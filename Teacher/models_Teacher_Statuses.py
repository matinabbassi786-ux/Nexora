from django.db import models
from django.contrib.auth.models import User
from .models_Teacher_Identification_Details import *



class Teacher_Statuses(models.Model):
  
    Employment_Status_OP= (
  
        ('Active','Active'),
  
        ('Inactive','Inactive'),
  
        ('Probation','Probation'),
  
        ('Permanent','Permanent'),
 
        ('Contract','Contract'),
 
        ('Part-Time','Part-Time'),
 
        ('Full-Time','Full-Time'),
 
        ('Intern','Intern'),
 
        ('Suspended','Suspended'),
 
        ('Resigned','Resigned'),
 
        ('Terminated','Terminated'),
 
        ('Retired','Retired'),
 
        ('Notice Period','Notice Period'),

    )
 
    Staff_working_Status_OP = (
 
        ('Working','Working'),
 
        ('Available','Available'),
 
        ('On Break','On Break'),
 
        ('In Class','In Class'),
 
        ('Teaching','Teaching'),
 
        ('Preparing Lessons','Preparing Lessons'),
 
        ('Checking Homework','Checking Homework'),
 
        ('Checking Exams','Checking Exams'),
 
        ('Student Consultation','Student Consultation'),
 
        ('Meeting','Meeting'),
 
        ('Training','Training'),
 
        ('Research','Research'),
 
        ('Remote Working','Remote Working'),
 
        ('On Campus','On Campus'),
 
        ('Offline','Offline'),
 
    )
 
    Attendance_Status_OP =(
 
        ('Present','Present'),
 
        ('Absent','Absent'),
 
        ('Half Day','Half Day'),
 
        ('On Leave','On Leave'),
 
        ('Holiday','Holiday'),
 
        ('Weekly Off','Weekly Off'),
 
    )

 
    role_op = (
 
        ('Junior Teacher','Junior Teacher'),
 
        ('Teacher','Teacher'),
 
        ('Senior Teacher','Senior Teacher'),
 
        ('Lead Teacher','Lead Teacher'),
 
        ('Principal','Principal'),
 
        ('Vice Principal','Vice Principal'),
 
        ('HR Director','HR Director'),
 
        ('CEO','CEO'),
 
        ('Manager','Manager'),
 
    )

 
    Teacher = models.OneToOneField(Teacher_Identification_Details,on_delete=models.CASCADE)
 
    Employment_status = models.CharField(Employment_Status_OP,max_length=100)
 
    Staff_working_Status = models.CharField(Staff_working_Status_OP,max_length=100)
 
    Work_From_Home = models.BooleanField(default=False)
 
    Last_Modification = models.DateTimeField(auto_now=True)
 
    Role = models.CharField(choices=role_op,max_length=100)
 
    Mentor = models.BooleanField(default=False)
 
    Private_Tutor = models.BooleanField(default=False) 