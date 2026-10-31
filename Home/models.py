from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField



# UserInfo model to store additional information about the user all encryption data is stored in the database and can be accessed by the Key only
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
    
    
    
    User_Bio = models.TextField(blank=True,null=True)
    
    User_OTP  = models.CharField(max_length=6,blank=True,null=True)
    
    User_Gender = models.CharField(max_length=1, choices=Gender_Choices)
    
    Is_Verified = models.BooleanField(default=False)
    
    User_Birth_Date = models.TextField()
    
    Last_Activity = models.DateTimeField(auto_now=True)
    
    First_Activity = models.DateTimeField(auto_now_add=True)
    

    
    slug = AutoSlugField(populate_from='User_Name', unique=True, always_update=True)

    Vital = models.TextField()

    Ip = models.TextField()    

    def __str__(self):
        return self.slug



class User_Status(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    USER_STATUS_CHOICES = (
        ("Active", "Active"),
        ("Inactive", "Inactive"),
        ("Pending", "Pending"),
        ("Blocked", "Blocked"),
        ("Suspended", "Suspended"),
        ("Banned", "Banned"),
        ("Locked", "Locked"),
        ("Under_Review", "Under_Review"),
        ("Expired", "Expired"),
        ("Deleted", "Deleted"),
    )

    user_status = models.CharField(max_length=75, choices=USER_STATUS_CHOICES)
    
    User_Activity_Status_Choices =(
     ("Online","Online"),   
     ("Offline","Offline"),   
     ("IDLE","IDLE"),   
     ("Busy","Busy"),   
     ("In_Class","In_Class"),   
     ("In_Meeting","In_Meeting"),   
     ("???","???"),   
    )

    User_Activity_Status = models.CharField(choices=User_Activity_Status_Choices,max_length=75,default="???")


class History(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    path = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

