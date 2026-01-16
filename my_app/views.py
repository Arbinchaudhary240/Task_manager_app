from django.shortcuts import render, get_object_or_404, redirect
from .models import Task
from .form import TaskForm

# Create your views here.

def index(request):
    return render(request, 'my_app/index.html')

def task_list(request):
    all_tasks = Task.objects.all()
    return render(request, 'my_app/task_list.html',{'tasks': all_tasks})

def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    return render(request, 'my_app/task_detail.html', {'task': task})

def create_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save() # This saves the new task to the database!
            return redirect('task_list') # Send user back to the list
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
