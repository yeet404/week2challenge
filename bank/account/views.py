from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

history = [
    ("withdraw", 2345),
    ("desposit", 234),
    ("withdraw", 2345),
    ("desposit", 234),
    ("withdraw", 2345),
    ("desposit", 234),
    ("withdraw", 2345),
    ("desposit", 234),
    ("withdraw", 2345),
    ("desposit", 234)
]

# Create your views here.
def index(request):
    return render(request, "account/index.html", {
        "name": "Yeet Fourzerofour"
    })

def bal(request):
    return render(request, "account/bal.html", {
        "history": history
    })

def transaction(request):
    return render(request, "account/transaction.html")