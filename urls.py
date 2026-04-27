from app import views  # ou le bon nom d'app

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]
