from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(req):
    return render(req,'shop/index.html')

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