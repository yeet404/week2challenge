from django.db.models import Sum
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Transaction

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        user_transactions = Transaction.objects.filter(user=request.user)
        balance = sum(user_transactions.values_list('amount', flat=True))
        return render(request, "user/index.html", {
            "transactions": user_transactions,
            "balance": balance
        })
    return HttpResponseRedirect(reverse("accounts:login"))

def transaction(request):
    if request.method == "POST":
        t = Transaction(transaction_type=request.POST["transaction-type"], amount=request.POST["money"], user=request.user)
        t.save()
        return render(request, "user/transaction.html", {
            "message": "Transaction completed successfully"
        })
    return render(request, "user/transaction.html")
