from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate

from .forms import *

# Create your views here.

def login_request(request):
    
    if request.method == 'POST':

        form= AuthenticationForm(request, data= request.POST)

        if form.is_valid():

            u= form.cleaned_data.get('username')
            p= form.cleaned_data.get('password')

            user= authenticate(username= u, password= p)

            if user:
                login(request, user)

                return render(request, 'store/products_list.html', {'message': f'Bienvenido { user }.'})
        
        else:

            return render(request, 'store/products_list.html', {'message': 'Datos incorrectos.'})
    
    else:

        form= AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def register(request):

      if request.method == 'POST':

            form= UserRegisterForm(request.POST)
            
            if form.is_valid():

                  username= form.cleaned_data['username']
                  
                  form.save()
                  
                  return render(request, 'store/products_list.html',  {'message': 'User created successfully.'})

      else:
                   
            form= UserRegisterForm()     

      return render(request, 'accounts/register.html',  {'form': form})



