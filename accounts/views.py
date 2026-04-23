from django.shortcuts import render, redirect
from .models import Profile

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
from django.shortcuts import render, redirect
from .models import Profile

def home(request):
    return render(request, 'accounts/home.html')

def register(request):
    return render(request, 'accounts/register.html')

def login_view(request):
    return render(request, 'accounts/login.html')
