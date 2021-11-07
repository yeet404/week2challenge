from django.db.models import Sum
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Transaction
from django.utils import timezone

# Create your views here.
def index(request):
    if request.user.is_authenticated:
        deposits = Transaction.objects.filter(transaction_type="DEPOSIT", user=request.user)
        withdrawals = Transaction.objects.filter(transaction_type="WITHDRAW", user=request.user)
        balance = sum(deposits.values_list('amount', flat=True)) - sum(withdrawals.values_list('amount', flat=True))
        return render(request, "user/index.html", {
            "transactions": Transaction.objects.filter(user=request.user),
            "balance": balance
        })
    return HttpResponseRedirect(reverse("accounts:login"))

def transaction(request):
    if request.method == "POST":
        # there's prob a better way to implement my bal check to reduce redundant code but idk lol
        deposits = Transaction.objects.filter(transaction_type="DEPOSIT", user=request.user)
        withdrawals = Transaction.objects.filter(transaction_type="WITHDRAW", user=request.user)
        try:
            balance = float(sum(deposits.values_list('amount', flat=True)) - sum(withdrawals.values_list('amount', flat=True)))
            amt = float(request.POST["money"])
        except ValueError:
            return render(request, "user/transaction.html", {
            "message": "Invalid entry."
        })
        t_type = request.POST["transaction-type"]
        if t_type == "WITHDRAW" and balance - amt < 0:
            return render(request, "user/transaction.html", {
            "message": "Insufficient funds"
        })
        t = Transaction(transaction_type=t_type, amount=amt, user=request.user, date=timezone.now())
        t.save()
        return render(request, "user/transaction.html", {
            "message": "Transaction completed successfully"
        })
    return render(request, "user/transaction.html")
