from django.db import models
from django.forms import DecimalField

# Create your models here.

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    inventory_quantity = models.IntegerField()