from django.db import models
from django.contrib.auth.models import User
from .models_Teacher_Identification_Details import *





class Teacher_Educational_Qualifications(models.Model):

    Teacher = models.OneToOneField(Teacher_Identification_Details,on_delete=models.CASCADE)

    Higher_Secondary = models.FileField(upload_to="Teacher/Higher_Secondary/",max_length=255)

    Degree = models.FileField(upload_to="Teacher/Degree/",max_length=255)

    Professional_op = (
        ("NTT","NTT"),

        ("D.El.Ed","D.El.Ed"),

        ("TGT","TGT"),

        ("PGT","PGT"),

        ("B.Ed","B.Ed"),

        ("M.Ed","M.Ed"),

    )

    Professional = models.CharField(max_length=50, choices=Professional_op)
