from django.db import models

from accounts.models import User


class Cash(models.Model):
    category = models.CharField(max_length=100, default='all')
    title = models.CharField(max_length=150)
    price = models.DecimalField(max_digits=15, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
