from django.contrib import admin
from django.urls import path
from ton_app import views  # 👈 adapte le nom

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),

    path('abonnes/', views.liste_abonnes, name='liste_abonnes'),  # 👈 AJOUT ICI
]
