from django.db import models
from Teacher.models import Teacher
from Student.models import Student_Info
from django.core.validators import MinValueValidator, MaxValueValidator



class Industry_List(models.Model):
    Industry = models.CharField(max_length=200)
    Industry_img = models.ImageField(upload_to="Industry/",max_length=250)
    date = models.DateTimeField(auto_now_add=True)


class Occupation_List(models.Model):

    Occupation = models.CharField(max_length=200)
    Occupation_img = models.ImageField(upload_to="Industry/Occupation/",max_length=250)
    date = models.DateTimeField(auto_now_add=True)

class Profession_List(models.Model):
    Profession = models.CharField(max_length=200)
    Profession_img = models.ImageField(upload_to="Industry/Occupation/Profession/",max_length=250)
    date = models.DateTimeField(auto_now_add=True)


class Specialization_List(models.Model):

    Specialization = models.CharField(max_length=200)
    Specialization_img = models.ImageField(upload_to="Industry/Occupation/Profession/Specialization/",max_length=250)
    date = models.DateTimeField(auto_now_add=True)

class Job_Role(models.Model):
    Job_Role = models.CharField(max_length=200)
    Job_Role_img = models.ImageField(upload_to="Industry/Occupation/Profession/Specialization/JobRole/",max_length=250)
    date = models.DateTimeField(auto_now_add=True)

class Skill(models.Model):

    Skill = models.CharField(max_length=200)
    Skill_img = models.ImageField(upload_to="Industry/Occupation/Profession/Specialization/JobRole/Skill/",max_length=250)
    date = models.DateTimeField(auto_now_add=True)

class Subject_list(models.Model):
    Subject = models.CharField(max_length=250)
    Subject_img = models.ImageField(upload_to="Industry/Occupation/Profession/Specialization/JobRole/Skill/Subject/")
    date = models.DateTimeField(auto_now_add=True)

class Course(models.Model):
    Course_Title = models.TextField()

    Course_Mine_Teacher = models.ManyToManyField(Teacher,related_name="Course_Mine_Teacher")

    Course_Sub_Teacher = models.ManyToManyField(Teacher,related_name="Course_Sub_Teacher")

    Industry = models.ManyToManyField(Industry_List,related_name="Industry2")
    Occupation = models.ManyToManyField(Occupation_List,related_name="Occupation1")

    Profession = models.ManyToManyField(Profession_List,related_name="Profession1")
    Specialization = models.ManyToManyField(Specialization_List,related_name="Specialization1")
    JobRole = models.ManyToManyField(Job_Role,related_name="JobRole1")
    
    skill = models.ManyToManyField(Skill,related_name="skill1")
    Subject = models.ManyToManyField(Subject_list,related_name="Subject1")

    Coin = models.PositiveIntegerField()
    Offer = models.PositiveSmallIntegerField(validators=[MinValueValidator(1),MaxValueValidator(100)],blank=True)
    Buyer_Student = models.ManyToManyField(Student_Info,related_name="Buyer_Student")
    
    Visitor_Total = models.PositiveBigIntegerField(default=0)
    like = models.ManyToManyField(Student_Info,related_name="like")
    Dislikes = models.ManyToManyField(Student_Info,related_name="Dislikes")
    

    Description = models.TextField()

    Management_Approval  = models.BooleanField(default=False)
    
    Main_All_Teacher_Approval  = models.BooleanField(default=False)
    
    Sub_All_Teacher_Approval  = models.BooleanField(default=False)

    
    img = models.FileField(upload_to="Course/img/")
    video = models.FileField(upload_to="Course/",blank=True,null=True)

    Crete_date = models.DateTimeField(auto_now_add=True)
    Last_date = models.DateTimeField(auto_now=True)

    pdf = models.FileField(upload_to="Course/pdf/")

    Code = models.TextField()

    slug = models.SlugField(unique=True)

class Course_Sub(models.Model):
    Courses = models.ForeignKey(Course,on_delete=models.CASCADE)
    
    Subject = models.ForeignKey(Subject_list,on_delete=models.CASCADE)
    main_title = models.TextField()
    
    pdf = models.FileField()
    video = models.FileField(upload_to="Course/sub/",blank=True,null=True)
    
    Crete_date = models.DateTimeField(auto_now_add=True)
    Last_date = models.DateTimeField(auto_now=True)

    main_Teacher_Approval  = models.BooleanField(default=False)

    Code = models.TextField()

    slug = models.SlugField(unique=True)


class Course_Sub_Sub(models.Model):
    Courses = models.ForeignKey(Course_Sub,on_delete=models.CASCADE)
    
    Subject = models.ForeignKey(Subject_list,on_delete=models.CASCADE)
    main_title = models.TextField()
    
    pdf = models.FileField()
    video = models.FileField(upload_to="Course/sub/",blank=True,null=True)
    
    Crete_date = models.DateTimeField(auto_now_add=True)
    Last_date = models.DateTimeField(auto_now=True)

    Main_Teacher_Approval = models.BooleanField(default=True)

    Teacher_Approval = models.BooleanField(default=False)

    Code = models.TextField()

    slug = models.SlugField(unique=True)

class Course_Score(models.Model):
    course = models.OneToOneField(Course,on_delete=models.CASCADE)
    
    Course_Knowledge_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Consistency_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Understanding_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Practical_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Assignment_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Exam_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
   
    Course_Test_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Project_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Completion_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Progress_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)

    Class_Room_live_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    
    Course_Consistency_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    

class Course_Score(models.Model):
    course_sub = models.OneToOneField(Course_Sub,on_delete=models.CASCADE)
    Subject_Knowledge_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    Concept_Understanding_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    Assignment_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    Test_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    Quiz_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    Completion_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)
    Class_Room_live_Score = models.IntegerField(validators=[MinValueValidator(-100),MaxValueValidator(100)],default=0)