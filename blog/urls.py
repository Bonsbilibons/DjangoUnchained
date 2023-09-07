from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('main/', views.main_page, name='main_page'),
]