from django.db import models
from Teacher.models import Teacher
from Student.models import Student_Info
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.

class Communication(models.Model):
    from_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="fromuser")
    to_user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="touser")
    description = models.TextField()
