from django.db import models
from django.contrib.auth.models import User
from .models_Student_Personal_Information import Student_Personal_Information



class Student_Contact_Information(models.Model):

    Student_Personal_Informations = models.OneToOneField(Student_Personal_Information,on_delete=models.CASCADE)

    Email_Address = models.TextField()

    PhoneNumber = models.TextField()