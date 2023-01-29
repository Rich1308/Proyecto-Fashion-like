from django.db import models as m
from django.contrib.auth.models import User

class adduser:
    def __init__(self,user,first_N,last_N,email,passwd):
        self.U = User.objects.create_user(username=user,first_name=first_N,last_name=last_N,email=email,password=passwd)
        self.U.save()

    



