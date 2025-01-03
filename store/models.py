
from django.db import models
import datetime
from django.core.files.storage import FileSystemStorage
from django.conf import settings
import os

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    

class Customer(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=55)
    password = models.CharField(max_length=255)
    email = models.EmailField()
    
    def __str__(self):
        return f'{self.first_name} {self.last_name}'
    

class Address(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    
    def __str__(self):
        return f'{self.city} {self.street} {self.zip}'

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(default='', max_length=500, blank=True, null=True) 
    image = models.ImageField(upload_to='uploads/products/', storage=FileSystemStorage(location=settings.MEDIA_ROOT))
    is_sale = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today, editable=True)

    def __str__(self):
        return  self.name

    def delete(self, *args, **kwargs):
    # Verifica se a imagem está sendo usada em outro produto
        if self.image:
            other_products = Product.objects.filter(image=self.image).exclude(pk=self.pk)
            if not other_products.exists():  # Apenas remove se nenhum outro produto estiver usando
                self.image.delete(save=False)
        super().delete(*args, **kwargs)


    def save(self, *args, **kwargs):
        if self.pk:
            old_instance = Product.objects.get(pk=self.pk)
            if old_instance.image and old_instance.image != self.image:
                # Verifica se a imagem antiga está em uso por outro produto
                other_products = Product.objects.filter(image=old_instance.image).exclude(pk=old_instance.pk)
                if not other_products.exists():  # Apenas remove se nenhum outro produto estiver usando
                    old_instance.image.delete(save=False)
        super().save(*args, **kwargs)

    
class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    phone = models.CharField(max_length=55, blank=True , null=True, default='')
    date = models.DateField(default=datetime.datetime.today, editable=False)
    values_status =  [
        ('pending', 'Pending'),
        ('accepted', 'Accepted'),
        ('rejected', 'Rejected')
    ]
    status = models.CharField(max_length=10, choices=values_status, default='pending')
    
    def __str__(self):
        return f'{self.product.name} {self.customer.first_name}'