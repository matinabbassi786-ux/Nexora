from django.db import models
from django.contrib.auth.models import User
from .models_Teacher_Identification_Details import *



class  Teacher_Address_Information(models.Model):

    Teacher = models.OneToOneField(Teacher_Identification_Details,on_delete=models.CASCADE)

    country = models.CharField(max_length=255)

    State = models.CharField(max_length=255)

    City = models.TextField()

    ZIPCode = models.CharField(max_length=250)

    Address = models.TextField()

    Mobile = models.TextField()

    Email = models.TextField()

    Emergency_Contact = models.TextField()