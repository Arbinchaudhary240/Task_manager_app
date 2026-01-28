from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

# Create your models here.
class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='task_image/', blank=True, null=True)
    due_date = models.DateTimeField(null=True, blank=True)

    PRIORITY_CHOICES = [
        ('L', 'Low'),
        ('M', 'Mediam'),
        ('H', 'High')
    ]
    priority = models.CharField(
        max_length= 1,
        choices = PRIORITY_CHOICES,
        default='M'
    )

    def __str__(self):
        return self.title
    
    @property
    def is_overdue(self):
        if self.due_date and not self.is_completed:
            return timezone.now() > self.due_date
        return False
    
    def get_notifications_status(self):
        if self.is_completed or not self.due_date:
            return None
        
        now = timezone.now()
        time_diff = self.due_date - now

        if time_diff.total_seconds() < 0:
            return "OVERDUE"
        
        if timedelta(hours=0) < time_diff <= timedelta(hours=1):
            # time_diff is > 0 and < 1 hours
            return "URGENT: Due is less than an hour"
        
        if self.due_date.date() == now.date():
            return "Remainder: Due Today"
        
        if self.due_date.date() == (now.date() + timedelta(days=1)):
            return "Upcoming: Due Tomorrow"