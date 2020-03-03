from django import forms
from django.db import models
from product.models import Product

# Create your form here

class ProductForm(forms.ModelForm):
    model = Product
    fields = "__all__"