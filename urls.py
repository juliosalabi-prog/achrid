from django.contrib import admin
from django.urls import path
from accounts import views   

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login_view, name='login'),
    path('register/', views.register, name='register'),
    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),
]
from accounts import views
