from django.shortcuts import render

# Create your views here.

def cart_summary(request):
    return render(request, 'cart.html', {})

def add_cart(request, id):
    # return render(request, 'cart.html', {})
    pass
def remove_cart(request, id):
    # return render(request, 'cart.html', {})
    pass
def update_cart(request, id):  
    # return render(request, 'cart.html', {})
    pass
