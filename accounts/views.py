from django.contrib.auth.models import User
from django.shortcuts import render, redirect

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(request, "register.html", {
                "error": "Ce nom d'utilisateur existe déjà"
            })

        User.objects.create_user(username=username, email=email, password=password)
        return redirect("login")

    return render(request, "register.html")
from django.shortcuts import render

def login_view(request):
    return render(request, "login.html")
from django.shortcuts import render
from .models import Abonne

def liste_abonnes(request):
    abonnes = Abonne.objects.all()
    return render(request, 'abonnes.html', {'abonnes': abonnes})
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

