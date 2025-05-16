from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    vat_id = models.CharField(max_length=30, unique=True, null=True, blank=True)
    street = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=30, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name