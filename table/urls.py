from django.urls import path
from . import views

app_name = 'table'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('tasks/', views.tasks,  name = 'tasks'),
    path('edit_task/', views.edit_task, name = 'edit_task'),
]