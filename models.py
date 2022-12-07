from django.db import models 

class User(models.Model):  
    user_name = models.CharField(max_length=50)  
    password = models.CharField(max_length=30)  
    email = models.CharField(max_length=70)

class Bill(models.Model):  
    date = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField() 

class BillDetails(models.Model):
    image = models.CharField(max_length=100)
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    price = models.IntegerField()
    intomoney = models.IntegerField()

class Category(models.Model):
    name = models.CharField(max_length=30)
    note = models.CharField(max_length=30)

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.CharField(max_length=100)
    vote = models.IntegerField()
    image = models.CharField(max_length=100)
    type = models.IntegerField()