from django.db import models
from django.contrib.auth.models import User
from .models_Teacher_Identification_Details import *
from django.core.validators import MaxValueValidator, MinValueValidator


class Teacher_Honorable(models.Model):

    Teacher = models.OneToOneField(Teacher_Identification_Details,on_delete=models.CASCADE)

    Honorable = models.IntegerField(
         validators=[MinValueValidator(-200), MaxValueValidator(200)]
    )


"""
3. Teacher honor scoring
Teacher activity	Points
Helping struggling students	+8
Mentoring students	+5
Supporting other teachers	+5
Creating useful learning resources	+5
Fair and transparent evaluation	+8
Consistent professional conduct	+5
Volunteering for academic support	+5
Providing constructive feedback	+3
Discrimination against students	-25
Harassment	-30
Deliberately unfair grading	-20
Sharing student private information	-25
Misusing student information	-30
Repeatedly neglecting responsibilities	-10
Academic dishonesty	-25
    """