from django.db import models
from django.contrib.auth.models import User

"""
    Stores a teacher's educational qualifications, certificates,
    professional experience documents and verification status.
"""
class Teacher_Educational_Qualifications(models.Model):
    Approval_Status_Opstion =(
        ("Pending","Pending"),
        ("Approved","Approved"),
        ("Rejected","Rejected"),
        ("On Hold","On Hold"),
        ("Escalated","Escalated"),
        ("Skipped","Skipped"),
        ("???","???"),
    )
    

    Approval_Status = models.CharField(choices=Approval_Status_Opstion,max_length=75,default="???")

    Date_Of_Joining = models.DateField()

    Leaving_Of_Joining = models.DateField(blank=True,null=True)
    
    User = models.OneToOneField(User,on_delete=models.CASCADE)
    Secondary = models.FileField(upload_to="Teacher/Secondary/")
    HigherSecondary = models.FileField(upload_to="Teacher/HigherSecondary/")
    Undergraduate = models.FileField(upload_to="Teacher/Undergraduate/")
    Postgraduate = models.FileField(upload_to="Teacher/Postgraduate/",blank=False,null=True)
    Diplomas = models.FileField(upload_to="Teacher/Postgraduate/",blank=False,null=True)
    Experience = models.FileField(upload_to="Teacher/Postgraduate/",blank=False,null=True)
    Final_Year_Marksheet = models.FileField(upload_to="Teacher/Design/",blank=True)



"""
    Manages teacher employment information, working availability,
    attendance, leave and organizational position.
"""
class Employment(models.Model):
    employment_status_op = (
        ("Active","Active"),
        ("Inactive","Inactive"),
        ("Probation","Probation"),
        ("Permanent","Permanent"),
        ("Contract","Contract"),
        ("Temporary","Temporary"),
        ("Part-time","Part-time"),
        ("Full-time","Full-time"),
        ("Intern","Intern"),
        ("Suspended","Suspended"),
        ("Resigned","Resigned"),
        ("Terminated","Terminated"),
        ("Retired","Retired"),
        ("Notice Period","Notice Period"),
        ("Onboarding","Onboarding"),
        ("Offboarding","Offboarding"),
        ("None","None"),
    )
    work_status_op = (
        ("Working","Working"),
        ("Available","Available"),
        ("Busy","Busy"),
        ("On Break","On Break"),
        ("In Meeting","In Meeting"),
        ("Work in Progress","Work in Progress"),
        ("Remote Working","Remote Working"),
        ("Work From Home","Work From Home"),
        ("Not Available","Not Available"),
        ("None","None"),
    )
    Attendance_status_op = (
        ("Present","Present"),
        ("Absent","Absent"),
        ("Half Day","Half Day"),
        ("On Leave","On Leave"),
        ("Weekly Off","Weekly Off"),
        ("Holiday","Holiday"),
        ("Holiday","Holiday"),
        ("None","None"),
    )
    Leave_status_op = (
        ("None","None"),
        ("On Leave","On Leave"),
        ("Sick Leave","Sick Leave"),
        ("Emergency Leave","Emergency Leave"),
        ("Emergency Leave","Emergency Leave"),
    )
    position_Op = (
        ("Junior Teacher","Junior Teacher"),
        ("Mid-Level Teacher","Mid-Level Teacher"),
        ("Senior Teacher","Senior Teacher"),
        ("Expert Teacher","Expert Teacher"),
        ("Principal","Principal"),
        ("Principal","Principal"),
        ("Manager","Manager"),
        ("HR","HR"),
        ("Admin","Admin"),
        ("Teaching Assistant","Teaching Assistant"),
        ("Tutor","Tutor"),
    )
    employment_status = models.CharField(choices=employment_status_op,max_length=100)
    work_status = models.CharField(choices=work_status_op,max_length=100)
    attendance_status = models.CharField(choices=Attendance_status_op,max_length=100)
    Leave_status = models.CharField(choices=Leave_status_op,max_length=100)
    position = models.CharField(choices=position_Op,max_length=100)

    User = models.OneToOneField(User,on_delete=models.CASCADE)


