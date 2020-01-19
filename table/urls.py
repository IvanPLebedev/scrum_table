from django.urls import path
from . import views

app_name = 'table'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('my_projects/', views.my_projects, name = 'my_projects'),
    path('my_projects/<project_id>/', views.project, name = 'project'),
    path('add_project/', views.add_project, name = 'add_project'),
    path('add_task/', views.add_task, name = 'add_task'),
]