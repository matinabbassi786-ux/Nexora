from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class UserInfo(models.Model):
    Gender_Choices = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    User_Name = models.TextField()
    First_Name = models.TextField()
    Last_Name = models.TextField()
    User_Email = models.TextField()
    User_Father_Name = models.TextField(blank=True,null=True)
    User_Mother_Name = models.TextField(blank=True,null=True)
    User_Bio = models.TextField(blank=True,null=True)
    User_OTP  = models.CharField(max_length=6,blank=True,null=True)
    User_Gender = models.CharField(max_length=1, choices=Gender_Choices)
    Is_Verified = models.BooleanField(default=False)
    Last_Activity = models.DateTimeField(blank=True, null=True)
    User_Birth_Date = models.TextField()
    First_Activity = models.DateTimeField(blank=True, null=True)
    User_Phone = models.ImageField(upload_to='user_photos/', blank=True, null=True)
