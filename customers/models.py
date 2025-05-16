from django.db import models

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=100)
    vat_id = models.CharField(max_length=30, unique=True)
    street = models.CharField(max_length=200)
    city = models.CharField(max_length=30)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.name