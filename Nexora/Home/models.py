from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator




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


class User_Online(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)  
    Online = models.BooleanField(default=True)  
    date = models.DateTimeField(auto_now_add=True)


class User_Path(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)  
    path = models.TextField()
    date = models.DateTimeField(auto_now_add=True)




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
    

class Honor(models.Model):
    Users = models.OneToOneField(User,on_delete=models.CASCADE)
    Student = models.BooleanField(default=False)
    Teacher = models.BooleanField(default=False)
    Management = models.BooleanField(default=False)
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)



class Honor_History(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE)
    Tite = models.CharField(max_length=255) 
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)
    date = models.DateField(auto_now_add=True)


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





