from django.db import models
from django.contrib.auth.models import User
from autoslug import AutoSlugField



#  the Profile_Code model is used to store the unique code for each user, which can be used for various purposes such as account verification or password reset. The Profile model is used to store additional information about the user, such as their bio, date of birth, gender, and activity timestamps.
class Profile_Code(models.Model):
    #  user name is used django default user model relationship is one to one
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    # Code unique is verification inside system 
    Code = models.TextField(max_length=500,unique=True)
    # Date news Created which date code is created 
    Date_Created = models.DateTimeField(auto_now_add=True)
    #  Date Updated last time code is updated
    Last_update = models.DateTimeField()
    #    slug is used to create a unique URL for each code instance, which can be used for various purposes such as account verification or password reset. The slug is generated automatically based on the Code field and is unique for each instance of the Profile_Code model.
    slug = AutoSlugField(populate_from='Code', unique=True)

# profile model is used to store additional information about the user, such as their bio, date of birth, gender, and activity timestamps.
class Profile(models.Model):
    
    # Gender Choices is selection field for user gender selection
    Gender_Choices = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )
    
    # User field is used create a one to one relationship with the default user model provided by django.
    User = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # A bio (short for biography) is a brief written summary of a person's life, work experience, achievements, or personality
    Bio = models.TextField(max_length=500, blank=True,null=True)
    
    # A birth date (or date of birth) is the calendar day, month, and year on which a person or thing was born
    Date_Birth = models.DateField()
    
    # Gender field is used to store the gender of the user
    Gender = models.CharField(max_length=10, choices=Gender_Choices)
    
    # An OTP (One-Time Password) is a temporary, single-use security code used to verify your identity during a login attempt or financial transaction.
    OTP = models.CharField(max_length=6,blank=True,null=True)
    
    #is_valid  check user otp is valid
    is_valid = models.BooleanField(default=False)
    
    # Last_Activity is  which lass time user is active in the system 
    Last_Activity = models.DateTimeField()
    
    #  Start_Activity is  which start time user is active in the system 
    Start_Activity = models.DateTimeField()
    
    # code is information about code
    code = models.OneToOneField(Profile_Code, on_delete=models.CASCADE)

    #    slug is used to create a unique URL for each code instance,
    slug = AutoSlugField(populate_from='code__Code')

    