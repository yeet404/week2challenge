from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts:login"))
    return redirect("/user/")

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("accounts:index"))
        else:
            return render(request, "accounts/login.html", {
                "message": "Invalid credentials."
            })
    return render(request, "accounts/login.html")

def logout_view(request):
    pass