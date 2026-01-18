# transactions/models.py
from django.db import models
from django.contrib.auth.models import User

class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('income', 'Income'),
        ('expense', 'Expense'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    amount = models.FloatField()
    category = models.CharField(max_length=50)
    transaction_type = models.CharField(choices=TRANSACTION_TYPES, max_length=10)
    date = models.DateField(auto_now_add=True)