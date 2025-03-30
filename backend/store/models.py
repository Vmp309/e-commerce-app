from django.db import models
import datetime

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Product (models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, blank=True, null=True)
    price = models.DecimalField(default=0, decimal_places=2, max_digits=6)
    image = models.ImageField(upload_to='uploads/product/', height_field=None, width_field=None, max_length=None)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)  
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=200, default='', blank=False)
    phone = models.CharField(max_length= 20)
    date = models.DateField(default=datetime.datetime.today)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.product


