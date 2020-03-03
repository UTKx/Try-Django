from django import forms
from django.db import models
from slider.models import Slider

class SliderForm(forms.ModelForm):
    model = Slider
    fields = "__all__"