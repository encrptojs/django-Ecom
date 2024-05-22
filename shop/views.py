from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(req):
    products = Product.objects.all()
    print(products)
    n = len(products)
    # print(products.0.image)
    nSlides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    return render(req,'shop/index.html',params)

def about(req):
    prod = Product.objects.get(product_name="AUTO")
    print("testing")
    print(prod.category)

    return render(req,"shop/about.html")     #retrieving from templates

def contact(req):
    return HttpResponse("Welcome to contact")

def tracker(req):
    return HttpResponse("Welcome to tracker")

def productView(req):
    return HttpResponse("Welcome to productView")

def search(req):
    return HttpResponse("Welcome to search")