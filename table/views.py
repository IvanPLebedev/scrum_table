from django.shortcuts import render
from .models import Status, Task
from .forms import TaskForm

from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
	return render(request, 'table/index.html')

def tasks(request):
    statuses = Status.objects.order_by('id')
    tasks = Task.objects.order_by('id')
    context = {'statuses': statuses, 'tasks': tasks}
    return render(request, 'table/tasks.html', context)

def edit_task(request):
    status = Status.objects.get(id = 1)# id = 1 - статус ICE BOX
    if request.method != 'POST':
        form = TaskForm()
    else:
        form = TaskForm(request.POST)
        if form.is_valid():
            new_task = form.save(commit = False)
            new_task.status = status
            new_task.save()
            return HttpResponseRedirect(reverse('table:tasks'))
    context = {'form': form}
    return render(request, 'table/edit_task.html', context)

