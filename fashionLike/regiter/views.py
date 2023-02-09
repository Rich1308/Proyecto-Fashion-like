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
import hashlib
import random

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

def myinner(person,user_id,countri_id,i=0):
    num1=person[i][user_id]
    num2=person[i][countri_id]
    newUs=list(Authuser.objects.filter(id=num1).values("user"))
    newUs2=list(Country.objects.filter(id=num2).values("country"))
    person[i][user_id] = newUs[0]["user"]
    person[i][countri_id] = newUs2[0]["country"]

def myinner_better(person,value_id,classe,value,i=0):
    num1=person[i][value_id]
    newUs=list(classe.objects.filter(id=num1).values(value))
    person[i][value_id] = newUs[0][value]
    """fuction  to make inner join"""
    

    
class Fashion_like(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get(self,request,id=None):
        try:
            people = list(adduser.objects.values())
        #print (adduser.objects.values())
            if id != None:
            #"First_Name","Last_Name","user","email","country"
                if id<1:
                    return HBR('Error, in the request, this resource not exist', status=404)
                else:
              
                    person = list(adduser.objects.filter(id=id).values())
                    #fuction created for my to make inner join
                    myinner_better(person,"user_id",Authuser,"user")
                    myinner_better(person,"country_id",Country,"country")
                    if len(person)==0:
                        return  HBR('Error, in the request, this resource not exist', status=404)
                    data = {
                            "message":"success 200",
                            "data":person 
                        }
                    return JR(data)

            if len(people)>0:
                for i in range(len(people)):
                    #myinner(people,"user_id","country_id",i)
                    myinner_better(people,"user_id",Authuser,"user",i)
                    myinner_better(people,"country_id",Country,"country",i)
                data = {
                    "message":"success 200",
                    "datapeople":people}
                return JR(data)
            else:   
                return HBR('Error, in the request', status=400)
        except:
            return HBR('Error, in the request,resource no found', status=404)

    def post(self,request):

        try:
            js = json.loads(request.body)
            print("1")
            if "user_A" in js and "password_A" in js:
                print("2")
                if not Authuser.objects.filter(user=js["user_A"]).exists() or not Authuser.objects.filter(password=js["password_A"]).exists():
                    return HBR('Error, user or password wrong ', status=403)

                u=list(Authuser.objects.filter(user=js["user_A"]).values("user"))
                p=list(Authuser.objects.filter(password=js["password_A"]).values("password"))
                #print(u[0]["user"],p[0]["password"])
                alet = random.random()
                my_token = hashlib.sha256((js["user_A"]+str(alet)).encode()).hexdigest()                      
                data = {
                        "message":"success 200",
                        "description":"the user was login successfuly", 
                        "token" : my_token,
                      }
                        
                return JR(data)


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
