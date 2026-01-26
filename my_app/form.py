from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type':'date', 'class':'form-control'},
                format='%Y-%m-%d'
            ),
        required=False
    )

    due_time = forms.TimeField(
        widget=forms.TimeInput(attrs={'type':'time', 'class':'form-control'}, format='%H:%M'),
        required=False
    )
    class Meta:
        model = Task
        fields = ['title', 'description', 'is_completed', 'priority','image']
    
    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)

        if self.instance and self.instance.due_date:
            self.fields['due_date'].initial = self.instance.due_date.date()
            self.fields['due_time'].initial = self.instance.due_date.time()