from django.shortcuts import render
from .models import Status, Task

def index(request):
	return render(request, 'table/index.html')

def tasks(request):
    statuses = Status.objects.order_by('id')
    tasks = Task.objects.order_by('id')
    context = {'statuses': statuses, 'tasks': tasks}
    return render(request, 'table/tasks.html', context)
