from django.urls import path
from account.views import *

urlpatterns = [
    path('register/', register),
    path('login/', login),
    path('logout/', logout)
]
