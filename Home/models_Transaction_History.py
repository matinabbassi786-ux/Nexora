from django.db import models
from django.contrib.auth.models import User


class Transaction_History(models.Model):

    Users = models.ForeignKey(User,on_delete=models.CASCADE)

    C_T_op = (

        ('Coins',"Coins"),

        ('Tickets',"Tickets"),

    )

    Bank_op = (

        ("Debit","Debit"),

        ("Credit","Credit"),

    )

    types = models.CharField(choices=C_T_op,max_length=50)

    Account = models.CharField(choices=Bank_op,max_length=50)

    Title = models.CharField(max_length=250)

    first_created = models.DateTimeField(auto_now_add=True)

    Amount = models.BigIntegerField()

    Balance = models.BigIntegerField()