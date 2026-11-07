from django.db import models
from django.contrib.auth.models import User
from .models_Student_Personal_Information import Student_Personal_Information






class  Studen_Academic_History_And_Program_Selection(models.Model):

    Student_Personal_Informations = models.OneToOneField(Student_Personal_Information,on_delete=models.CASCADE)

    Education_Level_OP =(

        ('High school','High school'),

        ('higher secondary','higher secondary'),

        ('graduation','graduation'),

        ('post-graduation','post-graduation'),

        ('None','None'),

    )

    Education_Level = models.CharField(choices=Education_Level_OP,max_length=255)

    School_or_Institution_Name = models.TextField()

    Academic_Year = models.TextField(max_length=250)

    Roll_Number_or_Student_ID = models.TextField()

    image_Roll_Number_or_Student_ID = models.ImageField(upload_to="Student/ID/")