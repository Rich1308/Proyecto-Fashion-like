from django.db import models as m
from django.contrib.auth.models import User

class adduser(m.Model):
    First_Name = m.CharField(max_length=20)
    Last_Name = m.CharField(max_length=20)
    user = m.CharField(max_length=15)
    password = m.CharField(max_length=20)
    email = m.CharField(max_length=50)
    country = m.CharField(max_length=30)

    



