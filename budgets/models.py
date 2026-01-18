from django.db import models
from django.contrib.auth.models import User

class Budget(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    month = models.DateField()
    total_budget = models.FloatField()
    goal_savings = models.FloatField()

    def __str__(self):
        return f"{self.user.username} - {self.month}"
