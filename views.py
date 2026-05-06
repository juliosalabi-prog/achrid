from django.shortcuts import render, redirect
from .models import Abonne

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


def home(request):
    return render(request, "home.html")


def liste_abonnes(request):
    abonnes = Abonne.objects.all()
    return render(request, "abonnes.html", {"abonnes": abonnes})
