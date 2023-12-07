from django import forms
from .models import Task

class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        exclude = ['assign_date', 'is_completed']
        widgets = {
            'catagories': forms.CheckboxSelectMultiple,
        }

class EditTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'catagories', 'is_completed']
        labels = {
            "is_completed": "Task completed"
        }
        widgets = {
            'catagories': forms.CheckboxSelectMultiple,
        }