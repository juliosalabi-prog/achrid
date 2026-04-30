from django.contrib import admin
from django.urls import path
from accounts import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),  # 👈 AJOUT ICI
]
from django.urls import path
from accounts import views
urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),
]

from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),
]
