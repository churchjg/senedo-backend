from django.db import models

# Create your models here.

class Home(models.Model):
    blank = models.CharField(max_length=100)
class Wine(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    pairings = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)

class Gift(models.Model):
    name = models.CharField(max_length=100)
    year = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)

class Gallery(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    
class Event(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    description = models.CharField(max_length=500)

class Checkout(models.Model):
    first = models.CharField(max_length=100)
    last = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=500)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=500)
    zip = models.CharField(max_length=100)
    country = models.CharField(max_length=500)
    cardname = models.CharField(max_length=100)
    cardnumber = models.CharField(max_length=100)
    expiration = models.CharField(max_length=100)
    cvv = models.CharField(max_length=500)
    