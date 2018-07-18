from django.contrib.auth import admin
from django.urls import path

from login import views

urlpatterns = [
    path('register', views.register),
    path('login_in',views.login_in),
]