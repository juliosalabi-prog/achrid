from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Abonne


def home(request):
    return render(request, 'home.html')


def liste_abonnes(request):
    abonnes = Abonne.objects.all()
    return render(request, 'abonnes.html', {'abonnes': abonnes})


def login_view(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        mot_de_passe = request.POST.get("mot_de_passe")

        Abonne.objects.create(
            contact=contact,
            mot_de_passe=mot_de_passe
        )
    return redirect("home")
    return render(request, "login.html")
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Abonne

def login_view(request):
    if request.method == "POST":
        contact = request.POST.get("contact")
        mot_de_passe = request.POST.get("mot_de_passe")

        if not contact or not mot_de_passe:
            return HttpResponse("Tous les champs sont obligatoires")

        Abonne.objects.create(
            contact=contact,
            mot_de_passe=mot_de_passe
        )

        return redirect("liste_abonnes")

    return render(request, "login.html")
