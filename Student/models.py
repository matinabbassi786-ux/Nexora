from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class   Student_Info(models.Model):
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


class Student_Score(models.Model):
    studen = models.OneToOneField(Student_Info,on_delete=models.CASCADE)
    
    Academic_Performance_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Knowledge_Mastery_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Homework_Quality_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Participation_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Academic_Integrity_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Critical_Thinking_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Creativity_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Consistency_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Improvement_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Learning_Progress_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Time_Management_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Overall_Student_Progress_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
