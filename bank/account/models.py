from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=8)
    amount = models.IntegerField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_maker", null=True)

    def __str__(self):
        return f"({self.user}) {self.transaction_type}: ${self.amount}"
