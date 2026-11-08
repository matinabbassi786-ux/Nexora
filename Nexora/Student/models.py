from django.db import models
from django.contrib.auth.models import User


class StudentAcademicBackground(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    Student_ID = models.TextField()
    Student_ID_PDF = models.FileField(upload_to="Student/Id/",max_length=255)
    Semester = models.TextField()
    School = models.TextField()
    Marksheet = models.FileField(upload_to="Student/Marksheet/")
