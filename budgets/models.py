from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, default='General')
    month = models.DateField()
    amount_limit = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.category} - {self.month}"

class Savings(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    target_amount = models.FloatField()
    current_amount = models.FloatField(default=0.0)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
