from django.db import models
from django.contrib.auth.models import User



class Teacher_Identification_Details(models.Model):
    class Gender(models.TextChoices):
       
        MALE = 'M', 'Male'
       
        FEMALE = 'F', 'Female'
       
        NON_BINARY = 'N', 'Non-Binary'
       
        OTHER = 'O', 'Other'
       
        PREFER_NOT_TO_SAY = 'P', 'Prefer not to say'


    Reservation_Statu_op=(
        ('SC','SC'),
        ('ST','ST'),
        ('OBC','OBC'),
        ('UR','UR'),
        ('Other','Other'),
    )

    Blood_Group_op = (
        ('A+','A+'),
        ('A-','A-'),
        ('B+','B+'),
        ('B-','B-'),
        ('AB+','AB+'),
        ('AB-','AB-'),
        ('O-','O-'),
        ('O+','O+'),
    )

    User = models.OneToOneField(User,on_delete=models.CASCADE)

    First_Name= models.TextField()

    Middle_Name= models.TextField()

    Last_Name= models.TextField()

    Father_Names =models.TextField(blank=True,null=True)

    Husband_Names =models.TextField(blank=True,null=True)

    Mother_Names =models.TextField(blank=True,null=True)

    Wife_Names =models.TextField(blank=True,null=True)

    Date_of_Birth = models.DateField()

    gender = models.CharField(
            max_length=1,
            choices=Gender.choices,
            default=Gender.PREFER_NOT_TO_SAY,
        )

    Mother_Tongue = models.CharField(max_length=255)

    Reservation_Statu = models.CharField(max_length=50,choices=Reservation_Statu_op)

    Blood_Group = models.CharField(max_length=50,choices=Blood_Group_op)

    Photograph =  models.ImageField(upload_to="Teacher/Photo/",max_length=255)

    Experience_Lette = models.FileField(upload_to="Teacher/Lette/",max_length=255,)

    Address = models.TextField()

    Teacher_Code = models.TextField()


    Date_leaving = models.DateField(blank=True, null=True )

    leaving = models.BooleanField(default=False)
