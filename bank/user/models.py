from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# DecimalField is based on max size of SQLite REAL datatype (8 bytes), but I have no clue if that matters lol
class Transaction(models.Model):
    transaction_type = models.CharField(max_length=8)
    amount = models.DecimalField(max_digits=22, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="transaction_maker", null=True)
    date=models.DateTimeField()

    def __str__(self):
        return f"({self.user}) {self.transaction_type}: ${self.amount} at {self.date}"
