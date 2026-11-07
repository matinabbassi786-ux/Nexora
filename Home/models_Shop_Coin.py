from django.db import models
from django.contrib.auth.models import User


class Shop_Coin(models.Model):

    title = models.CharField(max_length=255)

    Coin = models.CharField(max_length=255)

    Price = models.PositiveBigIntegerField(default=0)

    Is_Active = models.BooleanField(default=True)
