from django.shortcuts import render
from .models import Status, Task
from .forms import TaskForm, ChooseStatusForm

from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
	return render(request, 'table/index.html')

def tasks(request):
    statuses = Status.objects.order_by('id')
    tasks = Task.objects.order_by('id')
    context = {'statuses': statuses, 'tasks': tasks}
    return render(request, 'table/tasks.html', context)

def add_task(request):
    if request.method != 'POST':
        chooseStatusForm = ChooseStatusForm()
        taskForm = TaskForm()
    else:
        chooseStatusForm = ChooseStatusForm(request.POST)
        taskForm = TaskForm(request.POST)
        if taskForm.is_valid() and chooseStatusForm.is_valid():
            new_task = taskForm.save(commit = False)
            chosenStatus = chooseStatusForm.cleaned_data.get('status')
            new_task.status = status
            new_task.save()
            return HttpResponseRedirect(reverse('table:tasks'))
    context = {'taskForm': taskForm, 'statusForm': statusForm}
    return render(request, 'table/add_task.html', context)

