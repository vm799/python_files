from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.home, name="home"),  
    path('projects/', views.projects, name="projects"),
    path('work_experience/', views.work_experience, name="work_experience"),

]