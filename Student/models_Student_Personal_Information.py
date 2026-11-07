from django.db import models
from django.contrib.auth.models import User


class Student_Personal_Information(models.Model):

    class Gender(models.TextChoices):

        MALE = 'M', 'Male'

        FEMALE = 'F', 'Female'

        NON_BINARY = 'N', 'Non-Binary'

        OTHER = 'O', 'Other'

        PREFER_NOT_TO_SAY = 'P', 'Prefer not to say'


    User = models.OneToOneField(User,on_delete=models.CASCADE)

    FirstName = models.TextField()

    MiddleName = models.TextField()

    LastName = models.TextField()

    Date_of_Birth = models.DateTimeField()

    country = models.CharField(max_length=255)

    State = models.CharField(max_length=255)

    City = models.TextField()

    ZIPCode = models.CharField(max_length=250)

    Address = models.TextField()

    Student_Photo = models.ImageField(upload_to="Student/Photo/",max_length=255)

    Student_Code = models.TextField()

    Creation_time = models.DateTimeField(auto_now_add=True)

    Last_modification_time = models.DateTimeField(auto_now=True)

    gender = models.CharField(max_length=1,choices=Gender.choices,default=Gender.PREFER_NOT_TO_SAY,)