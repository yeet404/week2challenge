from django.db import models

# Create your models here.
class History(models.Model):
    transaction_type = models.CharField(max_length=8)
    amount = models.IntegerField()

    def __str__(self):
        return f"{self.transaction_type}: ${self.amount}"