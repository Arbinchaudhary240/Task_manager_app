from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('tasks/', views.TaskList.as_view(), name='task_list'),
    path('task-create/', views.TaskCreate.as_view(), name='create_task'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view(), name='task_detail'),
    path('tasks-update/<int:pk>/', views.TaskUpdate.as_view(), name='task_update'),
    path('tasks-delete/<int:pk>', views.TaskDelete.as_view(), name='task_delete'),
    path('register/', views.register, name='register'),
    path('tasl-toggle/<int:pk>/', views.TaskToggle.as_view(), name='task-toggle'),
]
