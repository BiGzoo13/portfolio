from django.contrib import admin
from django.urls import include, path
from project import views

urlpatterns = [
    path('', views.dashboard),
    path("<int:pk>/",views.project_detail),
    path('project/', views.project_index),

]