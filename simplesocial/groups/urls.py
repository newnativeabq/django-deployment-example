"""groups application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from groups import views as group_views

app_name = 'groups'

urlpatterns = [
    path('', group_views.ListGroups.as_view(), name='all'),
    path('new/', group_views.CreateGroup.as_view(), name='create'),
    path('posts/in/<slug:slug>/',group_views.SingleGroup.as_view(), name='single'),
    path('join/<slug:slug>/', group_views.JoinGroup.as_view(), name='join'),
    path('leave/<slug:slug>/', group_views.LeaveGroup.as_view(), name='leave'),
]