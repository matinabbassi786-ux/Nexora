from django.db import models
from Teacher.models import Teacher
from Student.models import Student_Info
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from Education.models import Course


class Course_Attendance(models.Model):
    Course_Name = models.ForeignKey(Course,on_delete=models.CASCADE)
    Student = models.ForeignKey(Student_Info,on_delete=models.CASCADE)
    data = models.DateTimeField()

class Course_Attendance(models.Model):
    Course_Name = models.ForeignKey(Course,on_delete=models.CASCADE)
    Student = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    data = models.DateTimeField()

class Student_Wabsit_Attendance(models.Model):
    Student = models.ForeignKey(Student_Info,on_delete=models.CASCADE)
    data = models.DateTimeField()

class Teacher_Wabsit_Attendance(models.Model):
    Student = models.ForeignKey(Teacher,on_delete=models.CASCADE)
    data = models.DateTimeField()


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


