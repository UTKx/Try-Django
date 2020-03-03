from django.urls import path
from product import views

urlpatterns = [
    path('', views.getProducts),
    path('details/<int:id>', views.productDetails, name='details')
]