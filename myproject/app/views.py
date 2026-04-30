from django.shortcuts import render,redirect
from .models import student
from .models import teacher

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
        return redirect('studentdata')
    return render(request,'studentform.html')


def teacherform(request):
    if request.method=='POST':
        empid=request.POST.get('empid')
        name=request.POST.get('name')
        email=request.POST.get('email')
        subject=request.POST.get('subject')
        teacher.objects.create(empid=empid,name=name,email=email,subject=subject)
        return redirect('teacherdata')
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