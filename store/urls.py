from django.urls import path
from .views import *

urlpatterns = [
    path('', Home.as_view(), name= 'Home'),
    path('products/<int:pk>', Products.as_view(), name= 'Products'),
    path('checkout/', checkout, name= 'Checkout')
]