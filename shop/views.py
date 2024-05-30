from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.
def index(req):

    allProds = []
    listCatIds = Product.objects.values('category','id')
    print(listCatIds)
    uniqueCats = {item['category'] for item in listCatIds}#storing only values for category
    print(uniqueCats)

    for item in uniqueCats:
        prod= Product.objects.filter(category=item) # unique list of item
        n = len(prod)
        nSlides = n//4 + ceil((n/4) - (n//4))
        allProds.append([prod, range(1,nSlides), nSlides]) # Collection of Unique Lists of item
        print("testing.........")
        print(prod)
    params = {'allProds':allProds}
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