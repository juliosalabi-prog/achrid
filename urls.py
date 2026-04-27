from app import views  # ou le bon nom d'app

urlpatterns = [
    path('', views.home, name='home'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
]

from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # 👈 IMPORTANT (page d’accueil)
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
]
from django.urls import path
from . import views

urlpatterns = [
    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),
]
