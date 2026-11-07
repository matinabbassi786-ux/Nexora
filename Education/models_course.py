from django.db import models

from Teacher.models_Teacher_Identification_Details import Teacher_Identification_Details

from Student.models_Student_Personal_Information import Student_Personal_Information

from .models_Skill import Skill

from .models_Subject import Subject

from .models_Field import Field

from .models_Industry import Industry

from .models_Topic import Topic

class Course(models.Model):
    DIFFICULTY_CHOICES = [
        ("Beginner", "Beginner"),
        ("Intermediate", "Intermediate"),
        ("Advanced", "Advanced"),
        ("Expert", "Expert"),
    ]

    TEACHING_MODE_CHOICES = [
        ("Live", "Live"),
        ("Recorded", "Recorded"),
        ("Live + Recorded", "Live + Recorded"),
    ]
    
    Title = models.TextField()
    
    description = models.TextField()

    
    Skills = models.ManyToManyField(Skill)
    
    Topics = models.ManyToManyField(Topic)
    
    Industrys = models.ManyToManyField(Industry)
    
    Fields = models.ManyToManyField(Field)
    
    Subjects = models.ManyToManyField(Subject)
    
    Image = models.ImageField(upload_to="Course/Image/",max_length=255)
    
    Lead_Instructors = models.ManyToManyField(Teacher_Identification_Details,related_name="Lead_Instructors")
    
    Supporting_Instructors = models.ManyToManyField(Teacher_Identification_Details,related_name="Supporting_Instructors")

    Buyer = models.ManyToManyField(Student_Personal_Information,related_name="Buyer")

    Enrollment_End = models.DateTimeField()
    
    Course_Duration = models.CharField(max_length=255)

    Language = models.CharField(max_length=255)

    Difficulty = models.CharField(max_length=255,choices=DIFFICULTY_CHOICES)
    
    Teaching_Mode = models.CharField(max_length=255,choices=TEACHING_MODE_CHOICES)
    
    Weekly_Hours = models.CharField(max_length=255)
    
    Course_Duration = models.CharField(max_length=255)

    Total_Student_Limit = models.PositiveBigIntegerField()

    Code = models.TextField()
    
    Course_price = models.PositiveBigIntegerField()
    
    Course_Bank_Coine = models.PositiveBigIntegerField()
    
    Course_Bank_Tickets = models.PositiveBigIntegerField()

    Rating = models.PositiveSmallIntegerField(default=0)

    Lead_Instructors_approval = models.BooleanField(default=False)
    
    Lead_Instructors_approval_List = models.ManyToManyField(Teacher_Identification_Details,blank=True,null=True)
    
    Supporting_Instructors_approval = models.BooleanField(default=False)
    
    Supporting_Instructors_approval_List = models.ManyToManyField(Teacher_Identification_Details,blank=True,null=True)
    
    Management_approval = models.BooleanField(default=False)




