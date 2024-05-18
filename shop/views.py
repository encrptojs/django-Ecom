from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(req):
    return render(req,'shop/index.html')

def about(req):
    return HttpResponse("Welcome to About")

def contact(req):
    return HttpResponse("Welcome to contact")

def tracker(req):
    return HttpResponse("Welcome to tracker")

def productView(req):
    return HttpResponse("Welcome to productView")

def search(req):
    return HttpResponse("Welcome to search")