from django.db import models
from django.contrib.auth.models import User

class User_Wallet(models.Model):

    Users = models.ForeignKey(User,on_delete=models.CASCADE)

    Coin = models.PositiveBigIntegerField(default=0)

    Ticket = models.PositiveBigIntegerField(default=0)
