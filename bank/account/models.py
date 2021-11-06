from django.db import models

# Create your models here.
class Username(models.Model):
    username = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.username}"


class Transaction(models.Model):
    transaction_type = models.CharField(max_length=8)
    amount = models.IntegerField()
    user = models.ForeignKey(Username, on_delete=models.CASCADE, related_name="transaction_maker")

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount}"
