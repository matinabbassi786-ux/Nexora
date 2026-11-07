from django.db import models
from django.contrib.auth.models import User
from .models_Teacher_Identification_Details import *
from django.core.validators import MaxValueValidator, MinValueValidator


class Teacher_History_Honorable(models.Model):
    Student = models.ForeignKey(Teacher_Identification_Details,on_delete=models.CASCADE)
    Title = models.CharField(max_length=255)
    Maker = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
