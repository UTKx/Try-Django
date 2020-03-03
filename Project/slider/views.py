from django.shortcuts import render
# from slider.forms import SliderForm
from slider.models import Slider
from product.models import Product

# Create your views here.

def index(request):
    slider = Slider.objects.all()
    return render(request, 'index.html', {"slider": slider})


