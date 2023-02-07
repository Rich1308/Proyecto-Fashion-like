from django.db import models as m
from django.contrib.auth.models import User

class Country(m.Model):
    country = m.CharField(max_length=30)
    def __str__(self) :
        return self.country

class Authuser(m.Model):
    user = m.CharField(max_length=15)
    password = m.CharField(max_length=20)

    def __str__(self) :
        return self.user

class adduser(m.Model):
    First_Name = m.CharField(max_length=20)
    Last_Name = m.CharField(max_length=20)
    #user = m.CharField(max_length=15)
    #password = m.CharField(max_length=20)
    email = m.CharField(max_length=50)
    #country = m.CharField(max_length=30)
    country = m.ForeignKey(Country,on_delete=m.CASCADE)
    user = m.ForeignKey(Authuser,on_delete=m.CASCADE)



    

    



