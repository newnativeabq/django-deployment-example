"""posts application URL Configuration

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
from . import views as post_views

urlpatterns = [
    path('', post_views.PostList.as_view(), name='all'),
    path('new/', post_views.CreatePost.as_view(), name='create'),
    path('by/<slug:username>', post_views.UserPosts.as_view(), name='for_user'),
    path('post/<slug:username>/<slug:pk>/', post_views.PostDetail.as_view(), name='post_single'),
    path('delete/<slug:pk>/', post_views.DeletePost.as_view(), name='delete'),
]