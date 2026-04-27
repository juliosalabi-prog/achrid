from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Abonne

def register(request):
    if request.method == "POST":
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        telephone = request.POST.get('telephone')

        Abonne.objects.create(
            nom=nom,
            email=email,
            telephone=telephone
        )

        return redirect('home')  # après enregistrement

    return render(request, 'register.html')
