from EasyLearn.views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns=[
	url(r'^login/$',login),
			url(r'^forgetpassword/$',forgetpassword,name="forgetpassword"),
			url(r'^editsubject/$',editsubject),
			url(r'^entersubdetail/$',entersubdetail),
			url(r'^registration/$',registration),
			url(r'^welcome/$',welcome),
			url(r'^auth_view/$',auth_view),
			url(r'^editcourse/$',editcourse),
			url(r'^addreview/$',addreview),
			
			url(r'^enter/$',enter),
			url(r'^addinfo/$',addinfo),
			url(r'^delete/$',delete),
			url(r'^deletecourse/$',deletecourse),
			url(r'^courses/$',courses),
			url(r'^subdetail/$',subdetail),
			
			url(r'^addcourse/$',addcourse),
			url(r'^entercourse/$',entercourses),
			url(r'^admin/$',admin),
			url(r'^logout/$',logout),
			url(r'^success/$',success),
			url(r'^contectus/$',contectus),
			url(r'^detailcourse/$',detailcourse),
			url(r'^aboutUs/$',aboutUs),
			url(r'^enterdetail/$',enterdetail),
			url(r'^addsubject/$',addsubject),
]