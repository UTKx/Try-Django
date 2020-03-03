from django.shortcuts import render
from product.models import Product

# Create your views here.

def getProducts(request):
    product = Product.objects.all()
    # print('AAAAAAAAAAAAAAAAAAAAAAAAAA')
    print('>>>>', product)
    return render(request, 'index.html', {"product": product})


def productDetails(request, id):
    detail = Product.objects.get(id=id)
    return render(request, 'single.html', {"detail": detail})
