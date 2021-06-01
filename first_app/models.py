from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=220)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    price = models.FloatField()
    description = models.TextField(max_length=1000)

    def __str__(self):
        return self.name

class Customer(models.Model):

    ## one to one with user as customer
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)

    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    pincode = models.IntegerField()
    address = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    ORDER_STATUS = (
    ("ORDERED","ORDERED"),
    ("PENDING","PENDING"),
    ("DELIVERED","DELIVERED"),
    ("SHIPPING","SHIPPING"),
    ("ARRIVING","ARRIVING")
    )
    order_status = models.CharField(max_length=150,choices=ORDER_STATUS)
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
