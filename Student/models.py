from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Student_Info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    Phone_Number = models.TextField()
    
    Parents_Number = models.TextField()
    Parents_Email = models.TextField()
    
    Mother_Name = models.TextField()
    
    Father_Name = models.TextField()
    
    Country = models.TextField(max_length=200)

    State = models.TextField()

    City = models.TextField()
    
    Town = models.TextField()

    Pin_Code = models.TextField()

    Address = models.TextField()

    Scholl_Or_College_No = models.TextField()

    Picter = models.ImageField(upload_to="Student/Picter/")


class Student_Documents(models.Model):
    Student = models.OneToOneField(Student_Info,on_delete=models.CASCADE)
    Marksheet = models.FileField(upload_to="Student/marksheet/", max_length=200,blank=True,null=True)
    Government_Id = models.FileField(upload_to="Student/id/", max_length=200,blank=True,null=True)
    Scholl_Or_College_Id = models.FileField(upload_to="Student/id/", max_length=200,blank=True,null=True)
    Scholl_Or_College_Degree = models.FileField(upload_to="Student/degree/", max_length=200,blank=True,null=True)
    Scholl_Or_College_Certificate = models.FileField(upload_to="Student/certificate/", max_length=200,blank=True,null=True)