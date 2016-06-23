from django.db import models
from django.contrib.auth.models import User
from PIL import Image
from time import time
from django.utils.timezone import now




# Create your models here.

def Person_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Person_%s/%s' % (instance.Person.id, filename)


def User_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'Person_%s/%s' % (instance.User.id, filename)


class Person(models.Model):
    NIC = models.CharField(unique=True,max_length=12)
    FName = models.CharField(max_length=30)
    LName = models.CharField(max_length=30)
    FullName = models.CharField(max_length=100)
    DOB = models.DateField(null=True)
    Nationality = models.CharField(max_length=20)
    AddressLine1 = models.CharField(max_length=100)
    AddressLine2 = models.CharField(max_length=100)
    AddressLine3 = models.CharField(max_length=100)
    AddressLine4 = models.CharField(max_length=100, null=True,blank=True)
    ContactNum = models.CharField(max_length=12)
    Email = models.EmailField(null=True,blank=True)
    FacebookProf = models.CharField(max_length=100,null=True,blank=True)
    LinkedInProf = models.CharField(max_length=100,null=True,blank=True)
    Date = models.DateField(default=now())
    PImage = models.FileField(upload_to= Person_directory_path,null=True,blank=True)
    Objective = models.TextField(null=True,blank=True)
    CVPDF = models.FileField(upload_to=Person_directory_path,null=True,blank=True)
    SpecialNotes = models.TextField(blank=True,null=True)
    Department = models.ManyToManyField("Department")
    Post = models.ManyToManyField("Post")
    Degree = models.ManyToManyField("Degree",through="Person_Degree")
    Interview = models.ManyToManyField("Interview",through='Person_Interview')

    def __str__(self):
        return self.FName,self.LName,self.FullName,self.Nationality


class Skill(models.Model):
    Skill = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Sports(models.Model):
    Sports = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)


class Extracurricular(models.Model):
    Extracurricular = models.TextField()
    person = models.ForeignKey("Person", on_delete=models.CASCADE)

class SpecialAchievements(models.Model):
    Person = models.ForeignKey(Person)
    Heading_1= models.CharField(max_length=100)
    Heading_2 = models.CharField(max_length=100)
    Notes = models.TextField()


class Person_Interview(models.Model):
    Person = models.ForeignKey(Person)
    Interview = models.ForeignKey("Interview")
    Interviewers =models.ManyToManyField("Interviewers",through='Person_Interview_viewer')


class Person_Interview_viewer(models.Model):
    Interviewers = models.ForeignKey('Interviewers')
    Person_Interview = models.ForeignKey(Person_Interview)
    Comment = models.TextField()
    Rate = models.PositiveSmallIntegerField()
    Status = models.ForeignKey("CV_Status")


class CV_Status(models.Model):
    Status = models.CharField(max_length=10)

    def __str__(self):
        return self.Status


class Department(models.Model):
    DeptName = models.CharField(max_length=30)

    def __str__(self):
        return self.DeptName




class InterviewType(models.Model):
    InterviewType = models.CharField(max_length=30)

    def __str__(self):
        return self.InterviewType


class Post(models.Model):
    Post = models.CharField(max_length=100)
    Field = models.CharField(max_length=100,null=True,blank=True)
    NoOfInterviews = models.PositiveIntegerField()
    InterviewType = models.ManyToManyField(InterviewType)
    degree  = models.ManyToManyField("Degree",through="Degree_For_Post")
    def __str__(self):
        return self.Post


class Post_Dept(models.Model):
    Post = models.ForeignKey('Post')
    Dept = models.ForeignKey('Department')

    def __str__(self):
        return self.Dept


class University(models.Model):
    university = models.CharField(max_length=100)
    def __str__(self):
        return self.university


class Degree(models.Model):
    University = models.ForeignKey(University)
    Degree = models.CharField(max_length=30)
    DegreeType = models.ForeignKey("DegreeType") #Phd ,BSc ,MSc
    DegreeField = models.ForeignKey("DegreeField") #Egineering,Bio Science,Arts,IT

    def __str__(self):
        return self.Degree,self.University


class DegreeField(models.Model):
    Field = models.CharField(max_length=100)

    def __str__(self):
        return self.Field


class DegreeType(models.Model):
    Type = models.CharField(max_length=10)
    HierachyNumber = models.IntegerField()
    def __str__(self):
        return self.Type


class Person_Degree(models.Model):
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)
    Degree = models.ForeignKey(Degree, on_delete=models.CASCADE)
    Year = models.DateField()
    SpecialNotes = models.TextField(null=True)
    Class = models.ForeignKey('Degree_class',null=True,blank=True)


class Degree_class(models.Model):
    Class =  models.CharField(max_length=20)

    def __str__(self):
        return self.Class


class UserRole(models.Model):
    Role = models.CharField(max_length=15)

    def __str__(self):
        return self.Role

class Degree_For_Post(models.Model):
    Degree = models.ForeignKey(Degree)
    Post = models.ForeignKey(Post)


class Users(models.Model):
    User = models.OneToOneField(User)
    FullName = models.CharField(max_length=100)
    Post = models.ForeignKey(Post)
    UPhoto = models.FileField(upload_to=User_directory_path,null = True,blank=True)
    Department = models.ForeignKey(Department)
    UserRole = models.ForeignKey(UserRole)


    def __str__(self):
        return self.UName


class Interviewers(Users):
    NoOfInts = models.PositiveIntegerField(null=True,blank=True)
    SpecializedArea = models.ManyToManyField('SpecializedArea')
    Interview = models.ManyToManyField("Interview")


class SpecializedArea(models.Model):
    SpecializedArea = models.CharField(max_length=100)


class Interview(models.Model):
    Time = models.TimeField()
    Date = models.DateField()
    Venue = models.ForeignKey('Venue')
    HOD = models.ForeignKey(User)
    Interviewers = models.ManyToManyField(User,related_name='User_Interviewer')
    Vacancy = models.ForeignKey('Vacancy')
    Department = models.ForeignKey(Department, on_delete=models.CASCADE)
    InterviewType = models.ForeignKey(InterviewType, on_delete=models.CASCADE)
    Interviewer_Review = models.TextField(blank=True,null=True)
    HOD_Review = models.TextField(blank=True,null=True)
    HR_Review = models.TextField(blank=True,null=True)
    NoOfPasses = models.PositiveIntegerField()
    NoOfFails = models.PositiveIntegerField()
    NoOfOnHolds = models.PositiveIntegerField()


class Venue(models.Model):
    HallName = models.CharField(max_length=40)

    def __str__(self):
        return self.HallName


class Vacancy(models.Model):
    DateOfPublish = models.DateField()
    ClosingDate = models.DateField()
    NoOfIntDone = models.IntegerField()
    NoOfPossitions = models.IntegerField()
    Post = models.ForeignKey(Post, on_delete=models.CASCADE)
    DeptID = models.ForeignKey(Department, on_delete=models.CASCADE)
    Post_Dept = models.ForeignKey(Post_Dept, on_delete=models.CASCADE)


class Experience(models.Model):
    Post = models.ForeignKey(Post,null=True,blank=True)
    AltPost = models.CharField(max_length=100,null=True,blank=True)
    Field = models.CharField(max_length=100)
    Duration = models.FloatField(max_length=2.2)
    Notes = models.TextField()
    Person = models.ForeignKey(Person,on_delete=models.CASCADE)

    def __str__(self):
        return self.Post,self.Type


class SubQualification(models.Model):

    QName = models.CharField(max_length=100)
    Subject = models.CharField(max_length=150)
    Result = models.CharField(max_length=10,null=True,blank=True)
    SubResult = models.CharField(max_length=4)
    QType = models.IntegerField() #if educational 1 or if professional 0
    person = models.ForeignKey("Person")
    SpecialNotes = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.Subject,self.SubResult


class subQul_Post(models.Model):
    QName = models.CharField(max_length=100)
    Subject = models.CharField
    SubResult =  models.CharField(max_length=10)
    Post = models.ForeignKey(Post)


class Exp_Post(models.Model):
    ExPost =  models.ForeignKey(Post,related_name='ExPost')
    Post = models.ForeignKey(Post)
    Duration = models.FloatField(max_length=2.2)


class Messages(models.Model):
    MsgType = models.IntegerField()
    MsgCont = models.TextField(null=True,blank=True)
    MsgAcceptance = models.IntegerField()
    Sender = models.ManyToManyField(User,through='Message_Send',related_name="Sender_User")
    Reciever = models.ManyToManyField(User,through='Message_Recieve',related_name="Reciever_User")


class Message_Send(models.Model):
    Sender = models.ForeignKey(User)
    Messages = models.ForeignKey(Messages)
    SentDate = models.DateField()
    SentTime = models.TimeField()


class Message_Recieve(models.Model):
    Reciever = models.ForeignKey(User)
    Messages = models.ForeignKey(Messages)
    RecievedDate = models.DateField()
    RecievedTime = models.TimeField()

