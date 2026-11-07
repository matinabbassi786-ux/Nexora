from django.db import models
from django.contrib.auth.models import User


class User_Info(models.Model):

    Status_op = (
        ('Active','Active'),

        ('Inactive','Inactive'),

        ('Pending Verification','Pending Verification'),

        ('Pending Approval','Pending Approval'),

        ('Suspended','Suspended'),

        ('Locked','Locked'),

        ('Deactivated','Deactivated'),

    )

    Delete = models.BooleanField(default=False)

    Users = models.OneToOneField(User,on_delete=models.CASCADE)

    Ip = models.TextField()

    Last_Ip = models.TextField()

    Code = models.TextField()

    Otp = models.CharField(max_length=255,null=True,blank=True)

    Unsafe = models.BooleanField(default=False)

    Safe = models.BooleanField(default=False)

    Suspicious = models.BooleanField(default=False)

    Validation = models.BooleanField(default=False)

    Create_By = models.DateTimeField(auto_now_add=True)

    Last_By = models.DateTimeField(auto_now=True)

    Coin = models.PositiveBigIntegerField(default=0)

    Ticket = models.PositiveBigIntegerField(default=0)

