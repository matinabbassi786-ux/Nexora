from django.db import models
from django.contrib.auth.models import User



class History_Path(models.Model):
    
    Users = models.ForeignKey(User,on_delete=models.CASCADE)
    
    Path = models.TextField()
    
    Create_By = models.DateTimeField(auto_now_add=True)
