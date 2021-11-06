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
        return HttpResponse("<p>yeet</p>")
    return render(request, "accounts/login.html")

def logout_view(request):
    pass