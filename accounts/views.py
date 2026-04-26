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

