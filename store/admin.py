from django.contrib import admin
from .models import Product, Category, Customer, Address, Order

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_discount','is_sale', 'sale_price')
    # fields = ('name', 'price', 'category', 'description', 'image', 'is_sale', 'is_discount', 'sale_price')


# Registra o modelo Product com a configuração personalizada ProductAdmin
admin.site.register(Product, ProductAdmin)
# Registra os outros modelos
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Address)
admin.site.register(Order)
