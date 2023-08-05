from django.urls import path
from . import views

urlpatterns = [
   
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('greeting/<str:username>', views.greeting, name='greeting'),
    path('projects/', views.projects, name='projects'),
    path('detailproject/<int:id>', views.detailproject, name='detailproject'),
    path('task/', views.task, name='task'),
    path('createtask/', views.createtask, name='createtask'),
    path('createprojects/', views.createprojects, name='createprojects'),
]
