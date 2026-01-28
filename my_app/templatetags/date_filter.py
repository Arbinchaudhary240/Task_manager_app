from django import template
from django.utils import timezone
from datetime import timedelta

register = template.Library()

@register.filter
def smart_date(value):
    if not value:
        return ""

    # Convert to local time 
    local_dt = timezone.localtime(value)
    today = timezone.localtime(timezone.now()).date()
    target_date = local_dt.date()
    
    time_str = local_dt.strftime("%I:%M %p")

    if target_date == today:
        date_label = "Today"
    elif target_date == today + timedelta(days=1):
        date_label = "Tomorrow"
    elif target_date == today - timedelta(days=1):
        date_label = "Yesterday"
    else:
        date_label = target_date.strftime("%b %d")

    return f"{date_label} at {time_str}"