from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import login_required


from .models import *

# Create your views here.

class Home(ListView):
    model= Products  

class Products(DetailView):
    model= Products

@login_required
def checkout(request):
    return render(request, 'store/checkout.html')