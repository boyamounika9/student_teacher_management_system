from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('home/',views.home,name='home'),
   path('studentform/',views.studentform,name='studentform'),
   path('teacherform/',views.teacherform,name='teacherform'),
   path('studentdata/',views.studentdata,name='studentdata'),
   path('teacher/',views.teacherdata,name='teacherdata'),
   path('studentupdate/<int:id>/',views.studentupdate,name='stuupdate'),
   path('studentdelete/<int:id>/',views.studentdelete,name='studelete'),
   path('teacherupdate/<int:id>/',views.teacherupdate,name='teaupdate'),
   path('teacherdelete/<int:id>/',views.teacherdelete,name='teadelete'),
   path('register/',views.register,name='register'),
   path('',views.loginpage,name='login'),
   path('logoutpage/',views.logoutpage,name='logout'),



   


]
