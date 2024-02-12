from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(blank=False)
    direction = models.CharField(max_length=100, blank=False)
    date = models.DateField(auto_now=True)

class Product(models.Model):
    name = models.CharField(max_length=100, blank=False)
    price = models.DecimalField(max_digits=8, decimal_places=2, blank=False)
    description = models.TextField(blank=False)
    sum = models.IntegerField(blank=False)
    date = models.DateField(auto_now=True)

class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    date_ordered = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=8, decimal_places=2)