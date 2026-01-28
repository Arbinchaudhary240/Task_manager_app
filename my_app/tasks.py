#This code is for future use and updates

# from celery import shared_task
# from .models import Task
# from django.utils import timezone
# from datetime import timedelta

# @shared_task
# def cheak_all_task_remainders():
#     now = timezone.now()
#     active_tasks = Task.objects.filter(is_comleted=False, due_date__isnull=False)

#     for task in active_tasks:
#         time_diff = task.due_date - now

#         if timedelta(hours=23) < time_diff <= timedelta(hours=24):
#             send_notification(task, "Remainder: This task is due tomorrow.")

#         elif timedelta(hours=7) < time_diff <=timedelta(hours=8):
#             send_notification(task, "Remainder: This task is due today.")

#         elif timedelta(minutes=50) < time_diff <= timedelta(hours=1):
#             send_notification(task, "URGENT: Due in 1 hour!")

#     def send_notification(task, message):
#         # For now, we print to the console
#         # Later, this will be your Email or Telegram code
#         print(f"--- NOTIFICATION FOR {task.user.username} ---")
#         print(f"Task: {task.title}")
#         print(f"Message: {message}")
        