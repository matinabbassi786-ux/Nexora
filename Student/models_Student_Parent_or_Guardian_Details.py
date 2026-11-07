from django.db import models
from django.contrib.auth.models import User
from .models_Student_Personal_Information import Student_Personal_Information





class Student_Parent_or_Guardian_Details(models.Model):

    GuardianRelationship_OP =(

        ("Legal Guardian","Legal Guardian"),

        ("Parent","Parent"),

        ("Stepparent","Stepparent"),

        ("Adoptive Parent","Adoptive Parent"),

        ("Foster Parent","Foster Parent"),

        ("Godparent","Godparent"),

        ("Conservator","Conservator"),

        ("Relative","Relative"),

    )

    Student_Personal_Informations = models.OneToOneField(Student_Personal_Information,on_delete=models.CASCADE)

    Guardian_Full_Name = models.TextField(choices=GuardianRelationship_OP,max_length=255)

    Phone_Number = models.TextField()

    Email = models.TextField()

    Address = models.TextField()
