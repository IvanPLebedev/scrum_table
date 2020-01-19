from django.urls import path
from . import views

app_name = 'table'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('my_projects/', views.my_projects, name = 'my_projects'),
    path('add_project/', views.add_project, name = 'add_project'),
    path('tasks/', views.tasks,  name = 'tasks'),
    path('add_task/', views.add_task, name = 'add_task'),
]