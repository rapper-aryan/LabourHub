from django.forms import ModelForm
from django.db import models

# Create your models here.

class Users(models.Model):
    id=models.AutoField(primary_key=True)
    fullname=models.CharField(max_length=100)
    aadhar=models.BigIntegerField()
    contact=models.BigIntegerField()
    password=models.CharField(max_length=50)
    status = models.CharField(max_length=50, default='FREE')

class Employees(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=100)
    email = models.EmailField()
    contact = models.BigIntegerField()
    password = models.CharField(max_length=50)

    #This function is used for converting object into String

    def __str__(self)-> str:
        return self.fullname