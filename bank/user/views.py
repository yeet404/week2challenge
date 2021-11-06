from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Transaction

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
    if request.user.is_authenticated:
        return render(request, "user/index.html", {
            "name": "Yeet Fourzerofour",
            "transactions": Transaction.objects.all() 
        })
    return HttpResponseRedirect(reverse("accounts:login"))

def transaction(request):
    if request.method == "POST":
        transaction = (request.POST["transaction-type"], int(request.POST["money"]))
        history.append(transaction)
        return render(request, "user/transaction.html", {
            "message": "Transaction completed successfully"
        })
    return render(request, "user/transaction.html")