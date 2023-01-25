from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.postgres.fields import JSONField
# Create your models here.
import base64
class Employee(models.Model):
    name=models.CharField(max_length=80)
    email=models.CharField(max_length=120,unique=True)
    age=models.IntegerField()
    gender=models.CharField(max_length=20)
    phoneNo=models.CharField(max_length=20)
    addressDetails=models.JSONField()
    workExperience=ArrayField(models.JSONField())
    qualifications=ArrayField(models.JSONField())
    projects=ArrayField(models.JSONField())
    photo=models.ImageField(upload_to='images',null=True,blank=True)








