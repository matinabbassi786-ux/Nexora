from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator



# ============================================================
# USER HISTORY
# Stores information about a user's browser, device, network,
# location, and environment whenever they access the platform.
# Useful for login history, security monitoring, and
# suspicious activity detection.
# ============================================================

class User_History(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)
    Ip = models.CharField(max_length=255)
    Browser = models.TextField()
    Operating_system = models.TextField()
    Device = models.TextField()
    Screen = models.TextField()
    Display = models.TextField()
    Network = models.TextField()
    Location = models.TextField()
    Time = models.TextField()
    Hardware = models.TextField()
    Storage = models.TextField()
    Browser_features = models.TextField()
    Battery = models.TextField()
    Permissions = models.TextField()
    red_flag  = models.BooleanField(default=False)
    green_flag  = models.BooleanField(default=False)
    gray_flag  = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)


# ============================================================
# USER PRIVACY AND ACCOUNT INFORMATION
# Stores additional account information, user roles,
# verification status, and account lifecycle information.
# One record is associated with one Django User.
# ============================================================

class User_privity(models.Model):
    Genders = (
        ("Male","Male"),
        ("Female","Female"),
        ("Other","Other"),
    )
    Account_Lifecycle_Status = (
        ('Active',"Active"),
        ('Inactive',"Inactive"),
        ('Deactivated',"Deactivated"),
        ('Deleted',"Deactivated"),
        ('Suspended',"Suspended"),
        ('Disabled',"Disabled"),
        ('Banned',"Banned"),
        ('Restricted',"Restricted"),
        ('Pending Verification',"Pending Verification"),
        ('Pending Deletion',"Pending Deletion"),
        ('Archived',"Archived"),
    )
    Users = models.OneToOneField(User,on_delete=models.CASCADE)
    Otp = models.CharField(max_length=255,blank=True,null=True)
    is_valid = models.BooleanField(default=True)
    Bio = models.TextField()
    Teacher = models.BooleanField(default=False)
    Student = models.BooleanField(default=False)
    Admin = models.BooleanField(default=False)
    Manager  = models.BooleanField(default=False)
    Inspector   = models.BooleanField(default=False)
    profile = models.ImageField(upload_to="profile/", max_length=255 )
    Account_Status = models.CharField(max_length=70,choices=Account_Lifecycle_Status)
    Code = models.TextField()


# ============================================================
# USER ONLINE STATUS
# Stores user online/offline status records.
# Can be used to track user activity and online sessions.
# ============================================================

class User_Online(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)  
    Online = models.BooleanField(default=True)  
    date = models.DateTimeField(auto_now_add=True)



# ============================================================
# USER PATH HISTORY
# Stores website paths or URLs visited by a user.
# Useful for activity tracking and navigation analytics.
# ============================================================

class User_Path(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)  
    path = models.TextField()
    date = models.DateTimeField(auto_now_add=True)











# ============================================================
# SHOP
# Stores products or packages available for purchase.
# Products can be purchased using supported wallet currencies.
# ============================================================
class Shop(models.Model):
    types =(
        ("Coin","Coin"),
        ("Ticket","Ticket"),
    )
    money = models.CharField(choices=types,max_length=50)
    Title = models.CharField(max_length=255)
    Price = models.PositiveIntegerField()
    type_total = models.PositiveIntegerField()
    date = models.DateTimeField(auto_now_add=True)
    


# ============================================================
# HONOR SYSTEM
# Stores the current honor and reputation score of a user.
# Each user has one Honor record.
# Separate honor categories are maintained for different roles.
# ============================================================

class Honor(models.Model):
    Users = models.OneToOneField(User,on_delete=models.CASCADE)
    Student = models.BooleanField(default=False)
    Teacher = models.BooleanField(default=False)
    Management = models.BooleanField(default=False)
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)

# ============================================================
# HONOR HISTORY
# Stores historical honor changes for each user.
# Every record represents an honor-related event or transaction.
# Useful for tracking reputation changes and auditing user behavior.
# ============================================================

class Honor_History(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)
    Tite = models.CharField(max_length=255) 
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)
    date = models.DateField(auto_now_add=True)



# ============================================================
# INDUSTRY
# Represents a broad economic or professional industry.
#
# Examples:
# Information Technology, Healthcare, Finance, Education.
#
# An industry can contain multiple fields and skills.
# A field can also belong to multiple industries.
# ============================================================

class Industry(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to="Image/Industry/",max_length=252)

    Field = models.ManyToManyField(
        "Field",
        blank=True,
        related_name="Industries"
    )

    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)

# ============================================================
# FIELD
# Represents a specialized area within one or more industries.
#
# Examples:
# Data Science, Software Development, Cybersecurity.
#
# A field can belong to multiple industries and contain
# multiple subjects.
# ============================================================

class Field(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to="Image/Field/",max_length=252)

    Industry = models.ManyToManyField(
        "Industry",
        blank=True,
        related_name="Fields"
    )

    Subject = models.ManyToManyField(
        "Subject",
        blank=True,
        related_name="Fields"
    )

    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)

# ============================================================
# SUBJECT
# Represents an academic or professional subject.
#
# Examples:
# Mathematics, Programming, Machine Learning, Economics.
#
# A subject can belong to multiple fields and contain
# multiple topics.
# ============================================================


class Subject(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to="Image/Subject/",max_length=252)

    Field = models.ManyToManyField(
        "Field",
        blank=True,
        related_name="Subjects"
    )

    Topic = models.ManyToManyField(
        "Topic",
        blank=True,
        related_name="Subjects"
    )

    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)


# ============================================================
# TOPIC
# Represents a specific knowledge area within a subject.
#
# Examples:
# Subject: Machine Learning
# Topics: Regression, Classification, Clustering.
#
# A topic can belong to multiple subjects and contain
# multiple skills.
# ============================================================

class Topic(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to="Image/Topic/",max_length=252)
    Subject = models.ManyToManyField(
        "Subject",
        blank=True,
        related_name="Topics"
    )

    Skill = models.ManyToManyField(
        "Skill",
        blank=True,
        related_name="Topics"
    )

    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)

# ============================================================
# SKILL
# Represents a practical ability or competency.
#
# Examples:
# Python Programming, Data Cleaning, SQL, Data Visualization.
#
# A skill can be relevant to multiple industries, fields,
# and topics.
# ============================================================
class Skill(models.Model):
    Name = models.CharField(max_length=255, unique=True)
    Description = models.TextField(blank=True, null=True)
    Image = models.ImageField(upload_to="Image/Topic/",max_length=252,null=True,blank=True)
    Industry = models.ManyToManyField(
        "Industry",
        blank=True,
        related_name="Skills"
    )

    Field = models.ManyToManyField(
        "Field",
        blank=True,
        related_name="Skills"
    )

    Topic = models.ManyToManyField(
        "Topic",
        blank=True,
        related_name="Skills"
    )

    Created_At = models.DateTimeField(auto_now_add=True)
    Updated_At = models.DateTimeField(auto_now=True)


# ============================================================
# BASIC IDENTIFICATION DETAILS
# Stores the personal identification and demographic
# information of a user.
#
# Each user has one basic identification record.
# Used for student, teacher, and other user verification.
# ============================================================

class Basic_Identification_Details(models.Model):
    Category_Op= (

        ("SC","SC"),
        ("ST","ST"),
        ("OBC","OBC"),
        ("Other","Other"),
    )
    Marital_Statuses = (
        ("Single","Single"),
        ("Married","Married"),
        ("Common-Law Married","Common-Law Married"),
        ("Engaged","Engaged"),
        ("Separated","Separated"),
        ("Divorced","Divorced"),
        ("Widowed","Widowed"),
    )
    Blood_Group_Op = (
        ('A-','A-'),
        ('B-','B-'),
        ('O-','O-'),
        ('AB-','AB-'),
        ('A+','A+'),
        ('B+','B+'),
        ('O+','O+'),
        ('AB+','AB+'),
    )
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    Date_of_Birth = models.DateField()
    Country = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    Zipcode = models.CharField(max_length=255)
    MobileNumber = models.TextField()
    Address  = models.TextField()
    MaritalStatuses = models.CharField(max_length=100,choices=Marital_Statuses)
    OtherEmail = models.TextField()
    OtherPhone = models.TextField()
    Wife = models.CharField(max_length=255,null=True,blank=True)
    husband = models.CharField(max_length=255,null=True,blank=True)
    Mother = models.CharField(max_length=255,null=True,blank=True)
    Father = models.CharField(max_length=255,null=True,blank=True)
    MotherTongue = models.CharField(max_length=255)
    Government_ID = models.TextField(max_length=255)
    Government_ID_pdf = models.ImageField(upload_to="User/Government/",max_length=255)
    Blood_Group = models.CharField(choices=Blood_Group_Op,max_length=50)

    Industrys = models.ManyToManyField(Industry)
    Fields = models.ManyToManyField(Field)
    Subject = models.ManyToManyField(Subject)





