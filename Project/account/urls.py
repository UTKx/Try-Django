from django.urls import path
from account.views import *

urlpatterns = [
    path('register/', register),
    # path('show/', show, name='show')
]
