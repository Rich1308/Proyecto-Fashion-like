#from django.shortcuts import render
from django.http import HttpResponse as HR
from .models import adduser
from django.template import loader

#Fuction for check user and password 
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HR("The user exist")
    else:
        return HR("The usern no exist")

def myform(request):
    user= request.POST['username']
    first_N = request.POST['first_name']
    last_N = request.POST['last_name']
    email = request.POST['email']
    passwd = request.POST['password']
    adduser(user,first_N,last_N,email,passwd)
    return HR("the register was succesful")

def showform(request):
    template = loader.get_template("regiter/myform.html")
    context = None
    return HR(template.render(context,request))

def showformregister(request):
    template = loader.get_template("regiter/myformreg.html")
    context = None
    return HR(template.render(context,request))

