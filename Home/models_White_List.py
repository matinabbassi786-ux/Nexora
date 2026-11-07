from django.db import models
from django.contrib.auth.models import User

class White_List(models.Model):

    Ip = models.TextField()

    Code = models.TextField()

    Create_By = models.DateTimeField(auto_now_add=True)
