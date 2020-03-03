from django.urls import path
from slider.views import *

urlpatterns = [
    path('', index, name='index'),
]