from django.db import models
from django.contrib.auth.models import User


class Per_Ticket_Price_In_Coin(models.Model):

    coin = models.PositiveIntegerField()

    Create_By = models.DateTimeField(auto_now_add=True)
