from django.db import models
from django.core.exceptions import ValidationError
from .options import *


def validate_email_iitb_domain(email):
    if email.split("@")[1] not in ["iitb.ac.in", "iitbombay.org"]:
        raise ValidationError(message="{} is not an valid email. It should end with iitb.ac.in or iitbombay.org".format(email))

def validate_email_not_ldap(email):
    return len(email.split("@")[0])==9 and str(email.split("@")[0][0]).isdigit()
# Create your models here.

# class Profile(models.Model):
#    name = models.CharField(max_length=100)
#    rollno = models.CharField(max_length = 100)
   # images = models.FileField(blank=True)

# class profileImages(models.Model):

       
#Model to store information during registration
class Student(models.Model):
    sso_id = models.CharField(primary_key = True, max_length = 9)
    first_name = models.CharField(max_length = 255, default = '', db_index = True)
    last_name = models.CharField(max_length = 255, default = '', db_index = True, blank=True)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def getNameTag(self):
        return "@"+str(self).replace(" ","_")
   

class Student_Profile(models.Model):
    student = models.OneToOneField(Student, on_delete = models.CASCADE, null = True)
    email = models.EmailField(null=False, blank=False, validators=[validate_email_iitb_domain])
    address = models.CharField(max_length=500, null=True, blank=True)
    personal_email = models.EmailField(null=False, blank=False, default='personal@gmail.com')
    
    dob = models.DateField(null = True, blank = True)
    profile_image = models.ImageField(null = True, blank=True)

    hostel_1 = '1'
    hostel_2 = '2'
    hostel_3 = '3'
    hostel_4 = '4'
    hostel_5 = '5'
    hostel_6 = '6'
    hostel_7 = '7'
    hostel_8 = '8'
    hostel_9 = '9'
    hostel_10 = '10'
    hostel_11 = '11'
    hostel_12 = '12'
    hostel_13 = '13'
    hostel_14 = '14'
    hostel_15 = '15'
    hostel_16 = '16'
    hostel_tansa = 'tansa'
    qip = 'qip'

    hostel_choices = (
        (hostel_1, 'Hostel 1'),
        (hostel_2, 'Hostel 2'),
        (hostel_3, 'Hostel 3'),
        (hostel_4, 'Hostel 4'),
        (hostel_5, 'Hostel 5'),
        (hostel_6, 'Hostel 6'),
        (hostel_7, 'Hostel 7'),
        (hostel_8, 'Hostel 8'),
        (hostel_9, 'Hostel 9'),
        (hostel_10, 'Hostel 10'),
        (hostel_11, 'Hostel 11'),
        (hostel_12, 'Hostel 12'),
        (hostel_13, 'Hostel 13'),
        (hostel_14, 'Hostel 14'),
        (hostel_15, 'Hostel 15'),
        (hostel_16, 'Hostel 16'),
        ('17', 'Hostel 17'),
        ('18', 'Hostel 18'),
        (hostel_tansa, 'Hostel Tansa'),
        (qip, 'QIP')
    )

    hostel = models.CharField(choices = hostel_choices, max_length = 255, null = True)
    room_no = models.CharField(blank = True, null = True, default = '101', max_length = 10)

    department = models.CharField(max_length = 255, null = True, choices = tuple([(dept, dept) for dept in DEPARTMENTS.keys()]))
    program = models.CharField(max_length = 30, null = True, choices = (('ug', 'Undergraduate'),('dd', 'Dual Degree'),('pg', 'Postgraduate'),('idddp','Inter-Disciplinary Dual Degree')))
    degree = models.CharField(max_length = 50, null = True, choices = DEGREES)
    join_year = models.IntegerField(null = True, default = 2017)
    graduation_year = models.IntegerField(null = True, default = 2021)

    nickname = models.CharField(max_length = 25, null = True, blank = True)
    tagline = models.CharField(max_length = 110, null = True, blank = True)

    ib_choices = tuple([(ib, ib) for ib in ACTIVITIES])

    ib1 = models.CharField(max_length = 255, null = True, blank = True)
    ib2 = models.CharField(max_length = 255, null = True, blank = True)
    ib3 = models.CharField(max_length = 255, null = True, blank = True)

    img1 = models.ImageField(null=True, blank=True)
    img2 = models.ImageField(null=True, blank=True)
    img3 = models.ImageField(null=True, blank=True)
    img4 = models.ImageField(null=True, blank=True)

    question1 = models.CharField(max_length = 100, null = True, blank = True, choices = [(question[0], question[1]) for question in QUESTIONS])
    answer1 = models.TextField(max_length = 300, null = True, blank = True)
    notification_preference = models.IntegerField(default=1, null=True, blank=True, choices=NOTIFICATION_PREFERENCES)
    details_done = models.BooleanField(default = False)

    def __str__(self):
        return str(self.student) + " Profile"
    #
    # def set_details_done(self, value):
    # 	print value
    # 	raise error
    # 	self.details_done=valuec

    def send_welcome_mail(self):
        emailid=self.email
        name=self.student.first_name
        html_content="<html><center><h2><p>Hello <div style='color:red;'>"+name+"</div> <br> Welcome to the <div style='color:red;'> Yearbook 2021! </div> Yearbook is an online portal by SARC, IITB for the entire IITB student community.<br> Share your memories, thoughts and sentiments for a period that'd eclipse our time at the institute.<br>"
        html_content+="<i>You can write messages for your friends who will be leaving institute this year.</i>"
        html_content+=' <br> <div style="color:red;"> #MyInsti_MySenti <br> #GetYearbooked </div>'
        html_content+="<br><br> Keep visiting the <a href='https://yearbook.sarc-iitb.org'>Yearbook Portal</a> and do follow the  <a href='https://www.facebook.com/SARC.IITB/'>SARC Page</a> for updates and informations.</p></h2></center></html>"
        text_content="Hello"+name+", we are very happy to have you here on yearbook."
        mail_subject="Welcome to Yearbook"


class Alum(models.Model):
    sso_id = models.CharField(primary_key = True, max_length = 9)
    email = models.EmailField(null=False, blank=False, validators=[validate_email_iitb_domain])