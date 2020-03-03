from django.db import models

# Create your models here.

class Slider(models.Model):
    name = models.CharField(max_length=100)
    image = models.FileField()

    class Meta:
        db_table = 'slider'