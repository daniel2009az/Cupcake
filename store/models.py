import os
from typing import Any
from django.db import models
import datetime
from django.core.files.storage import default_storage
from django.core.exceptions import ValidationError
from django.utils.html import mark_safe
from django.db.models.signals import post_delete
from django.dispatch import receiver


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
    image = models.ImageField(upload_to='uploads/products/')
    is_sale = models.BooleanField(default=False)
    is_discount = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0, max_digits=10, decimal_places=2, blank=True, null=True)
    date = models.DateField(default=datetime.datetime.today, editable=True)
    persistent_image = models.CharField(max_length=255, blank=True, null=True)

    def save(self, *args, **kwargs):
        # Se uma nova imagem foi carregada
        if self.image:
            # Gera um nome de arquivo único
            filename = f'uploads/products/{self.name}_{self.id}_{self.image.name}'
            
            # Salva a imagem no storage
            saved_path = default_storage.save(filename, self.image)
            
            # Atualiza o campo persistent_image com o caminho salvo
            self.persistent_image = saved_path
            
            # Limpa o campo de imagem original após salvar
            self.image = None

        super().save(*args, **kwargs)
    def __str__(self):
        return  self.name

@receiver(post_delete, sender=Product)
def delete_product_image(sender, instance, **kwargs):
    # Tenta deletar a imagem persistente
    if instance.persistent_image:
        try:
            default_storage.delete(instance.persistent_image)
        except Exception as e:
            print(f"Erro ao deletar imagem: {e}")

    
    
    
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