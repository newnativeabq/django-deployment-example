"""basic_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
"""
from django.urls import path, include
from . import views

app_name = 'basic_app'

urlpatterns = [
    path('', views.SchoolListView.as_view(), name='list'),
    path('create/', views.SchoolCreate.as_view(), name='create_school'),
    path('detail/<slug:pk>', views.SchoolDetailView.as_view(), name='school_detail'),
    path('update/<slug:pk>', views.SchoolUpdate.as_view(), name='update_school'),
    path('delete/<slug:pk>', views.SchoolDelete.as_view(), name='delete_school')
]