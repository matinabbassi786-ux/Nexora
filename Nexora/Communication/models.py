from django.db import models
from django.contrib.auth.models import User
from Teacher.models import Teacher
from Student.models import Student



class Followers(models.Model):
    Users = models.OneToOneField(User,on_delete=models.CASCADE,related_name="FollowerUsers")
    Follower =models.ManyToManyField(User,related_name="Follower")

class Following(models.Model):
    Users = models.OneToOneField(User,on_delete=models.CASCADE,related_name="Following_Users")
    Follower =models.ManyToManyField(User,related_name="Following")



class Message(models.Model):
    Froms_Users = models.ForeignKey(User,related_name="Froms_Users",on_delete=models.CASCADE)
    To_Users = models.ForeignKey(User,related_name="To_Users",on_delete=models.CASCADE)
    Messageing = models.TextField()
    read = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)