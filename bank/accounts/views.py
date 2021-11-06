from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("accounts:login"))
    return redirect("/user/")

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("user:index")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    
    form = UserCreationForm()
    return render (request=request, template_name="accounts/register.html", context={"form":form})

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
    logout(request)
    return render(request, "accounts/login.html", {
        "message": "Logged out."
    })
