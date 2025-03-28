from django.db import models

# Create your models here.
class Product (models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(max_length=500, blank=False)
    price = models.FloatField()
    image = models.ImageField(upload_to=None, height_field=None, width_field=None, max_length=None)
