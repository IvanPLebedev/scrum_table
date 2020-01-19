from django import forms

from .models import Status, Task, Project

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['name', 'description']
        labels = {'name':'Название прокта:', 'description': 'Описание:'}

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = ['title']
        labels = {'title': ''}

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title']
        labels = {'title': 'Задача:'}

class ChooseStatusForm(forms.Form):
    status = forms.ModelChoiceField(queryset = Status.objects.all(),
        label = 'Статус задачи')

