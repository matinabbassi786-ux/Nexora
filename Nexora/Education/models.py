from django.db import models
from Teacher.models import Teacher
from Student.models import Student
from Home.models import Subject,Industry,Field,Skill,Topic
from django.core.validators import MinValueValidator, MaxValueValidator



class Course(models.Model):
    leves_op = (
        ("Beginner","Beginner"),
        ("Intermediate","Intermediate"),
        ("Advanced","Advanced"),
    )

    Teaching_Mode_op = (
        ("Live + Recorded","Live + Recorded"),
        ("Live","Live"),
        ("Recorded","Recorded"),
    )


    Code = models.TextField()

    Title = models.TextField()

    Description = models.TextField()

    Rating = models.FloatField()

    Studenr_Limit  = models.PositiveIntegerField()

    Difficulty = models.CharField(choices=leves_op,max_length=50)

    After_price =  models.PositiveBigIntegerField()

    Before_price =  models.PositiveBigIntegerField()

    Course_Duration = models.TextField(max_length=255)

    Language = models.TextField()

    Teaching_Mode = models.CharField(max_length=250,choices=Teaching_Mode_op)
    
    LeadInstructors = models.ManyToManyField(Teacher,related_name="LeadInstructors")
    
    SupportingInstructors = models.ManyToManyField(Teacher,related_name="SupportingInstructors")
    
    Buyers =  models.ManyToManyField(Student)

    Industrys = models.ManyToManyField(Industry)
    
    Fields = models.ManyToManyField(Field)
    
    Subjects = models.ManyToManyField(Subject, through="Course_Subjects",related_name="Courses")
    
    Topics = models.ManyToManyField(Topic)
    
    Skills = models.ManyToManyField(Skill)

    Mine_Image = models.ImageField(upload_to="Course/",max_length=250)
    Enrollment_Ending  = models.DateTimeField()

    Created_At = models.DateTimeField(auto_now_add=True)

    Video = models.FileField(upload_to="Video/",max_length=250,null=True,blank=True)

    Mina_Image = models.FileField(upload_to="Video/",max_length=250)


    

class Course_Subjects(models.Model):
    Courses = models.ForeignKey(Course,on_delete=models.CASCADE,related_name="course_subjects")
    Subjects = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name="subjects")
    topics = models.ManyToManyField(Topic)
    Studeon_don = models.ManyToManyField(Student)
    Oder = models.IntegerField(default=0)
    
    Title = models.CharField(max_length=250)
    Description = models.TextField()

    Code = models.TextField()
    
    Mina_pdf = models.FileField(upload_to="pdf/",max_length=250,null=True,blank=True)
    Video = models.FileField(upload_to="Video/",max_length=250,null=True,blank=True)
    Mina_Image = models.FileField(upload_to="Image/",max_length=250,null=True,blank=True)



class Subjects_Topics(models.Model):

    Studeon_don = models.ManyToManyField(Student)
    Course_Subjecting = models.ForeignKey(
        Course_Subjects,
        on_delete=models.CASCADE

    )

    Topics = models.ForeignKey(Topic,on_delete=models.CASCADE,related_name="Course_Subjects_Topics")
    

    Order = models.PositiveIntegerField(default=0)

    Title = models.CharField(max_length=250)
    Description = models.TextField(blank=True)
    Code = models.TextField(blank=True)



class Courses_Honor(models.Model):
    Courses = models.OneToOneField(Course,on_delete=models.CASCADE)
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)


class Courses_Honor_History(models.Model):
    Users = models.ForeignKey(Courses_Honor,on_delete=models.CASCADE)
    Tite = models.CharField(max_length=255) 
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)
    date = models.DateField(auto_now_add=True)



class Courses_Subjects_Honor(models.Model):
    Courses = models.OneToOneField(Course_Subjects,on_delete=models.CASCADE)
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)


class Courses_Subjects_Honor_History(models.Model):
    Users = models.ForeignKey(Courses_Subjects_Honor,on_delete=models.CASCADE)
    Tite = models.CharField(max_length=255) 
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)
    date = models.DateField(auto_now_add=True)


class Courses_Subjects_Topic_Honor(models.Model):
    Courses = models.OneToOneField(Subjects_Topics,on_delete=models.CASCADE)
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)


class Courses_Subjects_Topic_Honor_History(models.Model):
    Users = models.ForeignKey(Courses_Subjects_Topic_Honor,on_delete=models.CASCADE)
    Tite = models.CharField(max_length=255) 
    Honor = models.FloatField(validators=[MinValueValidator(-100.0),MaxValueValidator(100.0)],default=0)
    date = models.DateField(auto_now_add=True)


