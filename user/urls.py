from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('home/', views.home, name='home'),  
    path('profile/', views.profile, name='profile'),
    path('devops/', views.devops, name='devops'),
    ]
