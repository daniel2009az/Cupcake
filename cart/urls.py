from django.urls import path
from . import views
# from django.conf import settings

urlpatterns = [
    path ('', views.cart_summary, name='cart'),

    path ('add/<int:id>/', views.add_cart, name='add_cart'),

    path ('remove/<int:id>/', views.remove_cart, name='remove_cart'),

    path ('update/<int:id>/', views.update_cart, name='update_cart'),


]