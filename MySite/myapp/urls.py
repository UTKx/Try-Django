from django.urls import path, re_path

from myapp.views import *

urlpatterns = [
    path('', index, name='index'),
    path('home/', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('add/', addData, name='add'),
    path('getshow/', getShow, name='getshow'),
    path('postshow/', postShow, name='postshow'),
    path('putdata/', putData, name='putdata'),
    path('showdata/', showData, name='showdata'),
    path('delete/<int:id>', delete, name='delete')
]