from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .form import TaskForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(task_list)
        
    else:
        form = UserCreationForm()
    return render(request, 'my_app/register.html', {'form': form})

@login_required
def task_list(request):
    search_input = request.GET.get('search-area') or ''

    tasks = Task.objects.filter(user=request.user)

    if search_input:
        tasks = tasks.filter(title__icontains=search_input)

    return render(request, 'my_app/task_list.html',{'tasks': tasks, 'search_input': search_input})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'my_app/task_detail.html', {'task': task})

@login_required
def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect('task_list') 
    else:
        form = TaskForm()
    
    return render(request, 'my_app/task_form.html', {'form': form})

def task_update(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save() # This saves the new task to the database!
            return redirect('task_detail', task_id=task.id) # Send user back to the list
    else:
        form = TaskForm(instance=task)
    
    return render(request, 'my_app/task_form.html', {'form': form, 'task': task})

def task_delete(request, task_id):
    task = get_object_or_404(Task, pk=task_id)

    if request.method == "POST":
        task.delete()
        return redirect('task_list')
    
    return render(request, 'my_app/task_confirm_delete.html', {'task': task})
