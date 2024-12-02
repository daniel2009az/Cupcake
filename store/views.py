from django.shortcuts import redirect, render
from .models import Product
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django import forms

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

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Voçe esta logado')
            return redirect('home')
        else:
            messages.error(request, 'Usuario ou senha invalidos')
            return redirect('login')
    return render(request, 'login.html', {})

def logout_user(request):
    logout(request)
    messages.success(request, 'Voçe esta deslogado')
    return redirect('home')

def register_user(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        for field in form:
            print("Field Error:", field.name,  field.errors)
        if form.is_valid():
            form.save() 
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password)  
            login(request, user)
            messages.success(request, 'Usuario cadastrado com sucesso')
            return redirect('home')
        else:
            print('else')
            messages.error(request, 'Erro ao cadastrar usuario')
            return redirect('register')
    else:
        print('else')
    return render(request, 'register.html', {'form': form})