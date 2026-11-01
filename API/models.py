from django.db import models
from Teacher.models import Teacher
from Student.models import Student_Info
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from Education.models import Course

# Create your models here.

class API_key(models.Model):
    key = models.TextField()
    user = models.OneToOneField(User,on_delete=models.CASCADE )
    data_new = models.DateTimeField()
    data_old = models.DateTimeField()

class Student_Code(models.Model):
    code = models.TextField()
    user = models.OneToOneField(Student_Info,on_delete=models.CASCADE )
    data_new = models.DateTimeField()
    data_old = models.DateTimeField()


class Teacher_Code(models.Model):
    code = models.TextField()
    user = models.OneToOneField(Teacher,on_delete=models.CASCADE )
    data_new = models.DateTimeField()
    data_old = models.DateTimeField()