from django import forms
from django.db import models
from category.models import Category

class CategoryForm(forms.ModelForm):
    model = Category
    fields = "__all__"