from django.db import models
from django.utils.translation import ugettext_lazy


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)
