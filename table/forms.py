from django import forms

from .models import Status, Task

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['title']
        labels = {'title': ''}


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        labels = {'title': ''}
