from django.db import models
from django.contrib.auth.models import User

class Wallet(models.Model):
    Users = models.OneToOneField(User,on_delete=models.CASCADE)  
    Coin = models.PositiveBigIntegerField(default=0)
    ticket = models.PositiveBigIntegerField(default=0)

class Coin_db(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE) 
    Coin = models.PositiveBigIntegerField(default=0)
    Buys = models.PositiveBigIntegerField(default=0)
    Code  = models.TextField()


class Ticket_db(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE) 
    Ticket = models.PositiveBigIntegerField(default=0)
    Buys = models.PositiveBigIntegerField(default=0)
    Code  = models.TextField()



class Payment_History(models.Model):
    bankings = (
        ("Credit","Credit"),
        ("Debit","Debit")
    )
    types =(
        ("Coin","Coin"),
        ("Ticket","Ticket"),
    )
    User = models.ForeignKey(User,on_delete=models.CASCADE)  
    money = models.CharField(choices=types,max_length=50)
    banking = models.CharField(choices=bankings,max_length=50)
    Title = models.CharField(max_length=255)
    balance = models.BigIntegerField()
    date = models.DateTimeField(auto_now_add=True)


class Pricing_Coin_to_Money(models.Model):
    Pricing = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class Ticket_To_Coin(models.Model):
    Pricing = models.PositiveIntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)


class Request_Payment_Refund(models.Model):
    Users = models.ForeignKey(User,on_delete=models.CASCADE) 
    text = models.TextField()
    approved = models.BooleanField(default=False)