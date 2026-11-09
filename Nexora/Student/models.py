from django.db import models
from django.contrib.auth.models import User
from Home.models import Subject,Industry,Field,Skill

class Student(models.Model):
    Student = models.OneToOneField(User,on_delete=models.CASCADE)
    Experience = models.CharField(max_length=250)
    StudentsTaught = models.TextField()
    Subjects = models.ManyToManyField(Subject)
    Industrys = models.ManyToManyField(Industry)
    Fields = models.ManyToManyField(Field)
    Skills = models.ManyToManyField(Skill)
    data = models.DateTimeField(auto_now_add=True)

class StudentAcademicBackground(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Student_ID = models.TextField()
    Student_ID_PDF = models.FileField(upload_to="Student/Id/",max_length=255)
    Semester = models.TextField()
    School = models.TextField()
    Marksheet = models.FileField(upload_to="Student/Marksheet/")
