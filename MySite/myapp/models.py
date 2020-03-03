from django.db import models

# Create your models here.

class Gareeb(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    address1 = models.TextField()
    address2 = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    
    class Meta:
        db_table = "gareeb"