#from django.shortcuts import render
from django.http import HttpResponse as HR , HttpResponseBadRequest as HBR
from .models import adduser,Country,Authuser
from django.template import loader
#Fuction for check user and password 
from django.contrib.auth import authenticate, login
from django.http.response import JsonResponse as JR
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
import json

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

    def get(self,request,id=None):
        people = list(adduser.objects.values())
        #print (adduser.objects.values())
        if id != None:
            #"First_Name","Last_Name","user","email","country"
            if id<1:
                return HBR('Error, in the request, this resource not exist', status=404)
            else:
              
                person = list(adduser.objects.filter(id=id).values())
                if len(person)==0:
                    return  HBR('Error, in the request, this resource not exist', status=404)
                data = {
                        "message":"success 200",
                        "data":person 
                    }
                return JR(data)

        if len(people)>0:
            data = {
                "message":"success 200",
                 "datapeople":people}
            return JR(data)
        else:   
            return HBR('Error, in the request', status=400)
        

    def post(self,request):

        try:
            js = json.loads(request.body)
            if Real("First_Name",js) and Real("Last_Name",js) and Real("user",js) and Real("password",js) and Real("email", js) and  Real("email",js) and Real("country",js):
                #print("error aqui")
                l_country = js["country"].lower()
                country2 = Country.objects.get(country=l_country).id
                #print("PAso")
                if Authuser.objects.filter(user=js["user"]).exists()==False:
                    Authuser.objects.create(user=js["user"],password=js["password"])   
                    #print("PAso2")
                    user2 = Authuser.objects.get(user=js["user"]).id
                    #print("PAso3",type(user2))
                    adduser.objects.create(First_Name=js["First_Name"],Last_Name=js["Last_Name"],email=js["email"],country_id=country2,user_id=user2)
                    #print("PAso4")
                    data = {
                        "message":"success 200",
                        "description":"the data was record successfuly" 
                    }
                    return JR(data)
                
                else:

                    return HBR('Error, The user already is exist', status=400)
                    
            else:
        
                return HBR('Erron in the data, some data no match with the format required', status=400)
        except:
            return HBR('Erron in the api', status=500)

    def path(self,request):
        pass

    def delete(self,request):
        pass

def index(request):
    template = loader.get_template("regiter/index.html")
    context = None
    return HR(template.render(context,request)) 
