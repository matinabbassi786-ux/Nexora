from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # ex Information Technology (IT)
    Industry = models.TextField()
    #  Software Development
    Occupation = models.TextField()
    #  Software Engineer
    Profession = models.TextField()
    #  Backend Developer
    Specialization = models.TextField()
    # Django Backend Developer
    Specific_Role = models.TextField()

    User_Father_Name = models.TextField(blank=True,null=True)
        
    User_Mother_Name = models.TextField(blank=True,null=True)

    Teacher_Id = models.TextField()

    Manager_Approval = models.BooleanField(default=False)

    Hr_Approval = models.BooleanField(default=False)

    Country = models.TextField(max_length=200)

    State = models.TextField()

    City = models.TextField()
    
    Town = models.TextField()

    Pin_Code = models.TextField()

    First_Address = models.TextField()
    
    First_Phone = models.TextField()
    
    First_Email = models.TextField()
    
    Second_Phone = models.TextField(blank=True,null=True)
    
    Second_Address = models.TextField(blank=True,null=True)
    
    Second_Email = models.TextField(blank=True,null=True)

    Approval_Status_Opstion =(
        ("Pending","Pending"),
        ("Approved","Approved"),
        ("Rejected","Rejected"),
        ("On Hold","On Hold"),
        ("Escalated","Escalated"),
        ("Skipped","Skipped"),
        ("???","???"),
    )

    Approval_Status = models.CharField(choices=Approval_Status_Opstion,max_length=75,default="???")

    Date_Of_Joining = models.DateField()

    Leaving_Of_Joining = models.DateField(blank=True,null=True)

    Leaving = models.BooleanField(default=False)


class Teacher_documents(models.Model):
    Teachers = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    Degree = models.FileField(upload_to="Teacher/Design/")
    Final_Year_Marksheet = models.FileField(upload_to="Teacher/Design/",blank=True)
    Resume = models.FileField(upload_to="Teacher/Design/",blank=True)
    Government_ID_Cards = models.FileField(upload_to="Teacher/Design/",blank=True)
    Certificate = models.FileField(upload_to="Teacher/Design/",blank=True)
    Experience_Letter = models.FileField(upload_to="Teacher/Design/",blank=True)

class Teacher_Score(models.Model):
    
    Teachers = models.OneToOneField(Teacher,on_delete=models.CASCADE)
    stages_Choices =(
        ("Fresher","Fresher"), # only helpe Student 
        ("Junior","Junior"), # can teach in class take mcq , other think teast other but not exam paper
        ("Mid-Level","Mid-Level"), # can teach without someone make wirte test 
        ("Senior","Senior"), # make wirte test masters make course exam paper
        ("Principal","Principal"), #
        ("Manager","Manager"),
        ("HR","HR"),
        ("Admin","Admin"),
        ("None","None"),
        ("???","???"),# unknow persone
    )
    Teacher_stages = models.CharField(choices=stages_Choices,max_length=25)
    
    Teaching_Quality_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Subject_Master_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Student_Support_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Reliability_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Preparation_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Classroom_Management_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Assessment_Quality_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Exam_Paper_Quality_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Test_Paper_Quality_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Crete_Quality_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Improvement_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Collaboration_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)

    Score_From_management = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)

    Overall_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)

    