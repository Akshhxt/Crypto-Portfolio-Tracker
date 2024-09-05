# portfolio/models.py

from django.db import models

class Cryptocurrency(models.Model):
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=20, decimal_places=10)
    change = models.DecimalField(max_digits=20, decimal_places=10, null=True, blank=True)
    volume = models.DecimalField(max_digits=30, decimal_places=10, null=True, blank=True)
    market_cap = models.DecimalField(max_digits=30, decimal_places=10, null=True, blank=True)
    icon_url = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name
