from django.shortcuts import render
from .models import Product


# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product(request, id): 
    product = Product.objects.get(id=id)
    return render(request, 'product.html', {'product': product})

def about(request):
    return render(request, 'about.html',  {})

def new(request):
    products = Product.objects.all()
    return render(request, 'new.html',  {'products': products})

def googleVerify(request):
    return render(request, 'google03bd2b58a927019e.html',  {})