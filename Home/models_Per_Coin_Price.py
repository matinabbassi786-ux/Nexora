from django.db import models
from django.contrib.auth.models import User


class Per_Coin_Price(models.Model):

    Money = models.PositiveIntegerField()

    Create_By = models.DateTimeField(auto_now_add=True)