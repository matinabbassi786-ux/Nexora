from django.db import models
from django.contrib.auth.models import User
from .models_Student_Personal_Information import Student_Personal_Information


class Student_History_Honorable(models.Model):
    
    Student = models.ForeignKey(Student_Personal_Information,on_delete=models.CASCADE)

    Title = models.CharField(max_length=255)
    
    Maker = models.IntegerField()
    
    created = models.DateTimeField(auto_now_add=True)

