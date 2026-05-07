from django.shortcuts import render,redirect
from .models import student
from .models import teacher
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError

# Create your views here.
def home(request):
    return render(request,'home.html')

def studentform(request):
    if request.method=='POST':
        rollnum=request.POST.get("rollnum")
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        branch=request.POST.get('branch')
        student.objects.create(rollnum=rollnum,name=name,age=age,email=email,branch=branch)
        messages.success(request, "Student details submitted successfully!")
        return redirect('studentdata')
    return render(request,'studentform.html')


def teacherform(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        teacher.objects.create(empid=empid,name=name,email=email,subject=subject)
        messages.success(request,'teacher details are submitted sucessfully!!')
        return redirect('teacherform')

    return render(request,'teacherform.html')

def studentdata(request):
    object=student.objects.all()
    return render(request,'studentdata.html',{'studata':object})

def teacherdata(request):
    object=teacher.objects.all()
    return render(request,'teacherdata.html',{'teachdata':object})

def studentupdate(request,id):
    obj1=student.objects.get(id=id)
    if request.method=='POST':
       obj1.rollnum=request.POST.get("rollnum")
       obj1.name=request.POST.get('name')
       obj1.age=request.POST.get('age')
       obj1.email=request.POST.get('email')
       obj1.branch=request.POST.get('branch')
       obj1.save()
       return redirect('studentdata')
    return render(request,'studentform.html',{'obj':obj1})



def teacherupdate(request,id):
    obj2=teacher.objects.get(id=id)
    if request.method=='POST':
       obj2.empid=request.POST.get("empid")
       obj2.name=request.POST.get('name')
       obj2.email=request.POST.get('email')
       obj2.subject=request.POST.get('subject')
       obj2.save()
       return redirect('teacherdata')
    return render(request,'teacherform.html',{'obj':obj2})


def studentdelete(request,id):
    object=student.objects.get(id=id)
    object.delete()
    return redirect('studentdata')

def teacherdelete(request,id):
    object=teacher.objects.get(id=id)
    object.delete()
    return redirect('teacherdata') 

#=======register page===============


def register(request):

    if request.method == 'POST':

        try:
            username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')
            cpassword = request.POST.get('cpassword')

            if password != cpassword:
                messages.warning(request, 'Password and Confirm Password do not match')
                return render(request, 'register.html')

            User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            messages.success(request,'registerd sucessfully !!!')
            return redirect('login')

        except IntegrityError:
            messages.error(request, 'User already exists')
            return render(request, 'register.html')

        except Exception as e:
            messages.error(request, f'Error: {e}')
            return render(request, 'register.html')

    return render(request, 'register.html')


def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Incorrect Credentials')
            return redirect('login')
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')