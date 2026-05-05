from django.contrib import admin
from django.urls import path
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('home/', views.home, name='home'),
    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),
]
