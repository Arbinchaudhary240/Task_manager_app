from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
        required=True
    )

    due_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type':'time', 'class':'form-control'}),
        required=False
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'priority','image']
        