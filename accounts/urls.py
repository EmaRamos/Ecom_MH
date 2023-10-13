from django.urls import path
from django.contrib.auth.views import LogoutView
from .views import *

urlpatterns = [
    path('login/', login_request, name= 'Login'),
    path('register/', register, name= 'SignUp'),
    path('logout/', LogoutView.as_view(template_name= "accounts/logout.html"), name= 'Logout')
]