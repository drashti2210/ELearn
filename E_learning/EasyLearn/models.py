from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Login(models.Model):
		Username=models.CharField(max_length=5,primary_key=True)
		Password=models.CharField(max_length=8)
class Login1(models.Model):
		Username=models.CharField(max_length=5,primary_key=True)
		Password=models.CharField(max_length=8)
		
class Student(models.Model):
		StudentId=models.CharField(max_length=5,primary_key=True)
		Password=models.CharField(max_length=8)
		Name=models.CharField(max_length=20)
		EmailId=models.CharField(max_length=50)
		
class Courses(models.Model):
		CourseId=models.CharField(max_length=12,primary_key=True)
		CourseName=models.CharField(max_length=20)
		
class Review(models.Model):
		Subjectname=models.CharField(max_length=12,primary_key=True)
		Comment=models.CharField(max_length=40)
class Subject(models.Model):
		SubjectID=models.CharField(max_length=5,primary_key=True)
		SubjectName=models.CharField(max_length=40)
		CourseId=models.ForeignKey(Courses,on_delete=models.CASCADE)
		Url=models.CharField(max_length=25,default="")

class CourseInfo(models.Model):
		#SubjectID=models.ForeignKey(Subject,on_delete=models.CASCADE)
		#CourseId=models.ForeignKey(Courses,on_delete=models.CASCADE)
		CourseName=models.CharField(max_length=40,primary_key=True)
		Introduction=models.CharField(max_length=9000)
		#Url=models.CharField(max_length=30,default="")
		#class Meta:
		#	unique_together=(('SubjectID','CourseId'))
class Subjectinfo(models.Model):
		
		Subjectname=models.CharField(max_length=12,primary_key=True)
		Subjectinfo=models.CharField(max_length=8000)
		Videourl=models.CharField(max_length=40)
		Docurl=models.CharField(max_length=40)
		ImageUrl=models.CharField(max_length=40) 
		
		
class Comments(models.Model):
		CommentId=models.CharField(max_length=5,primary_key=True)
		UserID=models.ForeignKey(Student,on_delete=models.CASCADE)
		Comment=models.CharField(max_length=500)
		SubjectID=models.ForeignKey(Subject,on_delete=models.CASCADE)
		
class Admin(models.Model):
		AdminId=models.CharField(max_length=5,primary_key=True)
		Password=models.CharField(max_length=8)
		Name=models.CharField(max_length=20)
		
class ReviewCourses(models.Model):
		
		SubjectID=models.CharField(max_length=12)
		Subjectname=models.CharField(max_length=12)
		Comment=models.CharField(max_length=40)
		StudentID=models.CharField(max_length=12,default="")
		Sname=models.CharField(max_length=12,default="")
	
class ReviewCourse1(models.Model):
		SubjectId=models.CharField(max_length=12,primary_key=True)
		Subjectname=models.CharField(max_length=12)
		Comment=models.CharField(max_length=40)