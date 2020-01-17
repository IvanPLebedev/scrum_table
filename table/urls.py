from django.urls import path
from . import views

app_name = 'table'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', views.tasks,  name = 'tasks'),
    path('add_task/', views.add_task, name = 'add_task'),
]