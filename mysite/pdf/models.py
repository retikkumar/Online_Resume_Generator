from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import DO_NOTHING
# Create your models here.

class Profile(models.Model):
    user_linked = models.ForeignKey(User,on_delete=models.CASCADE,related_name='+')
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    summary = models.TextField(max_length=1000)
    degree = models.CharField(max_length=200)
    school = models.CharField(max_length=200)
    university = models.CharField(max_length=200)
    previous_work = models.TextField(max_length=1000)
    skills = models.TextField(max_length=1000)
    projects = models.TextField(max_length=1000)


    
