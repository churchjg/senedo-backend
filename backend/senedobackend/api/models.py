from django.db import models

# Create your models here.

class Wine(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)