from django.shortcuts import render
from django.shortcuts import redirect

def index(request):
    return redirect("/user/")