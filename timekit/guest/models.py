from django.contrib.auth.models import User
from django.db import models
from django.forms import forms


class user(models.Model):
     first_name = models.CharField(max_length=60)
     last_name = models.CharField(max_length=60)
     email = models.CharField(max_length=60)
     timezone = models.CharField(max_length=50)
     created_at=models.DateTimeField(auto_now_add=True)
     updated_at=models.DateTimeField(auto_now_add=True)
     api_token=models.CharField(max_length=100, null=True)

class calender(models.Model):
     user=models.ForeignKey(user,related_name='user_id',null=True)
     name = models.CharField(max_length=20)
     description=models.CharField(max_length=250)
     cal_id=models.CharField(max_length=50)
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now_add=True)

class User_signup(models.Model):
     email = models.CharField(max_length=150)
     first_name = models.CharField(max_length=50)
     last_name = models.CharField(max_length=50)
     password = models.CharField(max_length=50)

class Animal(models.Model):
     name = models.CharField(max_length=40)
     sound = models.CharField(max_length=40)





