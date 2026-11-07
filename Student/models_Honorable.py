from django.db import models
from django.contrib.auth.models import User
from .models_Student_Personal_Information import Student_Personal_Information

from django.core.validators import MaxValueValidator, MinValueValidator


class Student_Honorable(models.Model):
    
    Student = models.OneToOneField(Student_Personal_Information,on_delete=models.CASCADE)
    
    Honorable = models.IntegerField(
         validators=[MinValueValidator(-200), MaxValueValidator(200)]
    )

    """
    2. Student honor scoring
Student activity	Points
Helping another student	+5
Helping a struggling student	+8
Sharing useful study resources	+3
Respecting teachers	+3
Participating positively	+2
Completing a group responsibility	+5
Reporting a genuine platform issue	+5
Consistent positive contribution	+10
Bullying another student	-15
Harassment	-25
Cheating in examinations	-20
Plagiarism	-15
Abusing teachers or students	-10
Deliberately disrupting classes	-8
Sharing examination answers illegally	-20
Repeated malicious behavior	-30
    """
