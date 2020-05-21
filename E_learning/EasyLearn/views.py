from django.shortcuts import render
import random
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.template.context_processors import csrf
from EasyLearn.views import *
from EasyLearn.templates import *
from EasyLearn.models import *
from django.contrib.auth.models import User,Group
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from django.views import generic

def login(request):
		c={}
		c.update(csrf(request))
		if  request.user.is_authenticated:
			return render(request,'welcome.html')
		return render(request,'login.html',c)
def addsubject(request):
		c={}
		c.update(csrf(request))
		return render(request,'addsubject.html',c)
def addcourse(request):
		c={}
		c.update(csrf(request))
		return render(request,'addcourse.html',c)
def entersubdetail(request):
		sname=request.POST.get('sname','')
		sinfo=request.POST.get('sinfo','')
		durl=request.POST.get('durl','')
		vurl=request.POST.get('vurl','')
		imgurl=request.POST.get('imgurl','')
		#print("sid is")
		#print(sid)
		s=Subjectinfo(Subjectname=sname,Subjectinfo=sinfo,Docurl=durl,Videourl=vurl,ImageUrl=imgurl)
		s.save();
		return render(request,'editsubject.html')
		
def enterdetail(request):
		sid=request.POST.get('sid','')
		cid=request.POST.get('cid','')
		sname=request.POST.get('sname','')
		url=request.POST.get('url','')
		print("sid is")
		print(sid)
		s=Subject(SubjectID=sid,SubjectName=sname,CourseId_id=cid,Url=url)
		s.save();
		return render(request,'addsubject.html')
def editsubject(request):
		#edit=CourseInfo.objects.all();
		return render(request,'editsubject.html')

def editcourse(request):
		edit=CourseInfo.objects.all();
		return render(request,'editcourse.html',{'edit':edit})
def admin(request):
		return render(request,"admin.html")
def addinfo(request):
		info=request.POST.get('text1','')
		cname=request.POST.get('cname','')
		s = CourseInfo(Introduction = info, CourseName=cname)
		s.save()
		return render(request,'editcourse.html')
def contectus(request):
		return render(request,'contectus.html')
def aboutUs(request):
		return render(request,'aboutUs.html')		
def detailcourse(request):
		cname=request.GET.get('cname')
		cid=request.GET.get('cid')
		print("cname is")
		print(cname)
		info=CourseInfo.objects.filter(CourseName=cname)
		list=Subject.objects.filter(CourseId_id=cid)
		request.session['sid']=list[0].SubjectID
		print(list)
		return render(request,"detailcourse.html",{'info':info,'list':list})
		
def entercourses(request):
	sname = request.POST.get('cid', '')
	sdate = request.POST.get('cname', '')
	s = Courses(CourseId = sname, CourseName=sdate)
	s.save()
	return render(request,'addcourse.html')

@login_required(login_url="/EasyLearn/login")
def courses(request):
	
	courseinfo = Courses.objects.all()
	
	print(courseinfo)

	return render(request,'courses.html', {'courseinfo':courseinfo})


def registration(request):
		userid=request.POST.get('sid')	
		password=request.POST.get('password')
		name=request.POST.get('name')
		email=request.POST.get('email')
		user=authenticate(username=userid,password=password)
		if user is None:
				user=User.objects.create_user(userid,email,password)
				user.save()
				#auth.login(request,user)
				s=Student(StudentId=userid,Password=password,Name=name,EmailId=email)
				s.save()
				#return HttpResponseRedirect('/EasyLearn/welcome/')
		return render(request,"login.html")
def enter(request):
			c={}
			c.update(csrf(request))
			return render(request,'registration.html',c)

			
def welcome(request):
		return render(request,"welcome.html")

@login_required(login_url="/EasyLearn/login")
def subdetail(request):
			
			name=request.GET.get('name')
		
			info=Subjectinfo.objects.filter(Subjectname=name)
			request.session['sname']=info[0].Subjectname

			review=ReviewCourses.objects.filter(Subjectname=name)
			#sprint(review[0].Subjectname)
			
			print("id issssss")
			#print(review[0].StudentID)
			#name=Student.objects.filter(review[0].StudentID)
			print("name iddddddd")
			#print(name[0].Name)
			print("info is")
			print(info)
			
		
			return render(request,"subdetail.html",{'subname':info,'review':review})
			
def addreview(request):
			subname=request.session['sname']
			
			info=Subject.objects.filter(SubjectName=subname)
			print("Id iss")
			
			print(info[0].SubjectID)
			cmt=request.POST.get('cmt')
			sid=request.session['id']
			sname=request.session['name']
			s=ReviewCourses(Subjectname=subname,Comment=cmt,SubjectID=info[0].SubjectID,StudentID=sid,Sname=sname)	
			s.save()
			review=ReviewCourses.objects.filter(Subjectname=sname)

			return render(request,"success.html")
def success(request):
			return render(request,"success.html")
def delete(request):
			cid=request.POST.get('cid','')
			print("cid isss")
			print(cid)
			Courses.objects.filter(CourseId=cid).delete()
			return render(request,'welcome.html')	
def deletecourse(request):
			
			
				return render(request,'deletecourse.html')
		
							
def auth_view(request):
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if request.user.is_authenticated:
			request.session['session']="Learn"
			user1=Student.objects.filter(Name=username)
			return render(request,'welcome.html')
		
		
		
		
		#print(username)
		#print(password)
		#user=User.objects.get(username=username)
		#print(user)
		user=authenticate(username=username,password=password)
		
		if user :
			auth.login(request,user)
			user1=Student.objects.filter(StudentId=username)
			if user1:
				request.session['id']=user1[0].StudentId
				request.session['name']=user1[0].Name
			return render(request,"welcome.html",{'user1':user1})
		else:
			messages.add_message(request,messages.WARNING,'Incorrect')
			return render(request,'login.html')
def forgetpassword(request):
			a=random.randint(1000000,9000000)
			send_mail("This for new password","password is"+str(a),"avinavekariya6@gmail.com",["avinavekariya6@gmail.com"],fail_silently=False)
			return render(request,'login.html')
def logout(request):
				print("logout")
				
				auth.logout(request)
				c={}
				c.update(csrf(request))
				request.session['session']=None
				request.session['id']=None
				request.session['name']=None
				request.session['session']=None
				return render(request,'login.html')