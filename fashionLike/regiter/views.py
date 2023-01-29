from django.shortcuts import render
from django.http import HttpRequest as HR
from .models import adduser

#Fuction for check user and password 
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return 
    else:
        return 

def myform(request):
    username = request.POST['username']
    password = request.POST['password']
    
    u = adduser()
