#from django.shortcuts import render
from django.http import HttpResponse as HR , HttpResponseBadRequest as HBR
from .models import adduser
from django.template import loader
#Fuction for check user and password 
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse as JR
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json


"""
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
    return HR(template.render(context,request))"""

def Real(name,di):
    """Fuction to review the data  that come from request"""
    list1 = ['#','*','+','_','@','-','%','~','=','$'] #password characters
    count = 0 #General counter
    count2 = 0 #variable to control the point '.'
    up = 0 #variable to control the number of upper in password
    up2 = 0 #variable to control the number in password
    up3 = 0 #variable to control the number lower in password
    a = di[name]
    if not isinstance(a,str):
        return False
    if len(a) == 0:
        return False
    if a.isspace():
        return False
    if name == "First_Name" or name == "Last_Name" or name== "country":
        if not a.isalpha():
            return False
    elif name == "password":
        if len(a) < 8 or len(a)>15:
            return False 
        for i in a:
            if i in list1:
                count = count +1 
            if i.isupper():
                up +=1
            if i.isnumeric():
                up2 +=1
            if i.islower():
                up3 +=1
        if count == 0 or up==0 or up2 ==0 or up3==0:
            return False

    elif name == "email":
        for i in a:
            if i=='@':
                count +=1
            if i=='.':
                count2 +=1
        if count == 1 and count2 == 1:
            return True
        return False
    return True


    
class Fashion_like(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request):
        pass

    def post(self,request):
        try:
            js = json.loads(request.body)
            if Real("First_Name",js) and Real("Last_Name",js) and Real("user",js) and Real("password",js) and Real("email", js) and  Real("email",js) and Real("country",js):
                adduser.objects.create(First_Name=js["First_Name"],Last_Name=js["Last_Name"],user=js["user"],password=js["password"],email=js["email"],country=js["country"])
                data = {
                    "message":"success 200",
                    "description":"the data was record successfuly" 
                }
                return JR(data)
            else:
                #data = {
                 #   "message": "error in the data", 
                  #  "error":"400"
                #}
                return HBR('Erron in the data, some data no match with the format required', status=400)
        except:
            data = {"message":"error"}
            return JR(data)

    def path(self,request):
        pass

    def delete(self,request):
        pass

def index(request):
    template = loader.get_template("regiter/index.html")
    context = None
    return HR(template.render(context,request)) 
