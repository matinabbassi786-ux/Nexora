from django.db import models
from django.db import models
from Teacher.models import Teacher
from Student.models import Student_Info
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User



class Notifications(models.Model):
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    Title  = models.TextField()
    description = models.TextField()
    Read = models.BooleanField(default=False)
    created_data = models.DateField(auto_now_add=True)
    Read_data = models.DateField(auto_now_add=True)


