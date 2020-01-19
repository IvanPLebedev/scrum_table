from django.shortcuts import render
from .models import Status, Task, Project
from .forms import TaskForm, ChooseStatusForm, ProjectForm

from django.http import HttpResponseRedirect
from django.urls import reverse

def index(request):
	return render(request, 'table/index.html')

def my_projects(request):
    projects = Project.objects.order_by('id')
    context = {'projects': projects}
    return render(request, 'table/my_projects.html', context)

def project(request, project_id):
    project = Project.objects.get(id = project_id)
    statuses = project.status_set.order_by('id')
    tasks = []
    if statuses:
        for status in statuses:
            tasks += status.task_set.order_by('id')
    context = {'project': project,'statuses': statuses, 'tasks': tasks}
    return render(request, 'table/project.html', context)


def add_project(request):
    if request.method != 'POST':
        projectForm = ProjectForm()
    else:
        projectForm = ProjectForm(request.POST)
        if projectForm.is_valid():
            projectForm.save()
            return HttpResponseRedirect(reverse('table:my_projects'))
    context = {'projectForm': projectForm}
    return render(request, 'table/add_project.html', context)

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
    context = {'taskForm': taskForm, 'statusForm': chooseStatusForm}
    return render(request, 'table/add_task.html', context)

