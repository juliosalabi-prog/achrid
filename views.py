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
    telephone=telephone,
    est_valide="@" in email if email else False
)        )

        return redirect('home')  # après enregistrement

    return render(request, 'register.html')
from django.shortcuts import render
from .models import Abonne

def liste_abonnes(request):
    abonnes = Abonne.objects.all()
    return render(request, 'abonnes.html', {'abonnes': abonnes})
