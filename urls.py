from app import views  # ou le bon nom d'app

urlpatterns = [
    path('', views.home, name='home'),
]
