from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    image = models.FileField()
    category = models.CharField(max_length=50)
    description = models.TextField()

    class Meta:
        db_table = 'product'