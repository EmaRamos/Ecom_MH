from django.db import models
import datetime

# Create your models here.

# Categories of Products
class Categories(models.Model):
    name= models.CharField(max_length= 50)

    def __str__(self):
        return f' Category: {self.name}'
    
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

# Products
class Products(models.Model):
    name= models.CharField(max_length= 50)
    description= models.CharField(max_length= 100, default= '', blank= True, null= True)
    price= models.DecimalField(default= 0, max_digits= 8, decimal_places= 2)
    category= models.ForeignKey(Categories, on_delete= models.CASCADE, default= 1)
    image= models.ImageField(upload_to= 'uploads/products/')
    is_sale= models.BooleanField()
    sale_price= models.DecimalField(default= 0, max_digits= 8, decimal_places= 2)

    def __str__(self):
        return f' Product: {self.name}'
    
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

# Customers
class Customers(models.Model):
    first_name= models.CharField(max_length= 50)
    last_name= models.CharField(max_length= 50)
    phone= models.CharField(max_length= 10)
    email= models.EmailField()
    password= models.CharField(max_length= 50)
    
    def __str__(self):
        return f' Customer: {self.first_name} {self.last_name}'
    
    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'

# Orders
class Orders(models.Model):
    product= models.ForeignKey(Products, on_delete= models.CASCADE)
    customer= models.ForeignKey(Customers, on_delete= models.CASCADE)
    quantity= models.IntegerField(default= 1)
    address= models.CharField(max_length= 50, default= '', blank= False)
    phone= models.CharField(max_length= 10, default= '', blank= False)
    date= models.DateField(default= datetime.datetime.today)
    status= models.BooleanField(default= False)

    def __str__(self):
        return f' Order: {self.id}'
    
    class Meta:
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'
