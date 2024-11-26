from django.urls import path
from . import views



urlpatterns = [
    path('', views.home,  name='home'),

    path('product/<int:id>/', views.product, name='product'),

    path('about/', views.about, name='about'),
    
    path('new/', views.new, name='new'),

]