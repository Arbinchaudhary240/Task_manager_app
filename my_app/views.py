from django.shortcuts import render, redirect
from .models import Task
from .form import TaskForm
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.views import View
from django.utils import timezone
import datetime

# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')

def register(request):
    if request.user.is_authenticated:
        return redirect('task_list') # Don't let the logged in user register again.
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task_list')
        
    else:
        form = UserCreationForm()
    return render(request, 'my_app/register.html', {'form': form})

class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'my_app/task_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # 1. Filter tasks by the current user
        user_tasks = context['tasks'].filter(user=self.request.user)
        
        # 2. Get the search input
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            user_tasks = user_tasks.filter(title__icontains=search_input)
        
        # 3. Update the context with the filtered tasks and the count
        context['tasks'] = user_tasks
        context['count'] = user_tasks.filter(is_completed=False).count() # Use user_tasks, not context['count']
        context['search_input'] = search_input
    
        return context

class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'my_app/task_detail.html'
    
class TaskCreate(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = "Task was created sucessfully!"
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        date = form.cleaned_data.get('due_date')
        time = form.cleaned_data.get('due_time')

        if date:
            if not time:
                time = datetime.time(23, 59)
            combined = datetime.datetime.combine(date, time)
            form.instance.due_date = timezone.make_aware(combined)

        return super().form_valid(form)
    
class TaskUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    success_url = reverse_lazy('task_list')
    success_message = "Task was updated succesfully"

    def form_valid(self, form):
        form.instance.user = self.request.user
        date = form.cleaned_data.get('due_date')
        time = form.cleaned_data.get('due_time')

        if date:
            if not time:
                time = datetime.time(23, 59)
            combined = datetime.datetime.combine(date, time)
            form.instance.due_date = timezone.make_aware(combined)

        return super().form_valid(form)
    
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name= 'tasks'
    success_url = reverse_lazy('task_list')
    template_name = 'my_app/task_confirm_delete.html'

    def get_success_url(self):
        messages.success(self.request, "Task deleted successfully.")
        return reverse_lazy('task_list')
    
class TaskToggle(LoginRequiredMixin, View):
    def get(self, request, pk):
        task = Task.objects.get(id=pk, user=request.user)
        task.is_completed = not task.is_completed
        task.save()
        return redirect('task_list')