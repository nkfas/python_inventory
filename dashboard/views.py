from django.shortcuts import render,redirect
from . models import *


# Create your views here.
def index(request):
    return render(request,'dashboard/index.html')

def Registration(request):
    if request.method=='POST':
        name=request.POST['username']
        password=request.POST['password']
        emailaddress=request.POST['emailaddress']
        mobileno=request.POST['mobileno']
        
        salesman=Salesman(name=name,password=password,emailaddress=emailaddress,mobileno=mobileno,active=0)
        salesman=Salesman.objects.filter(name=name).exists()
        if salesman:
            message='User already exists'
            return render(request,'dashboard/Registration.html',{'msg':message})
        else:
          salesman=Salesman(name=name,password=password,emailaddress=emailaddress,mobileno=mobileno,active=0)  
          salesman.save()
        return redirect('dashboard:viewuser')
    return render(request,'dashboard/Registration.html')
def viewuser(request):
    users=Salesman.objects.all()
    return render(request,'dashboard/viewusers.html',{'defuser':users})

def UserActive(request,sid):
    salesman=Salesman.objects.get(id=sid)
    if salesman.active==0:
        Salesman.objects.filter(id=sid).update(active=1)
    else:
        Salesman.objects.filter(id=sid).update(active=0)
    return redirect('dashboard:viewuser')
def UserDelete(request,sid):
    Salesman.objects.get(id=sid).delete()
    return redirect('dashboard:viewuser')

def updateuser(request,sid):
    salesman=Salesman.objects.get(id=sid)
    if request.method=='POST':
        name=request.POST['name']

        salesman.name=name
        salesman.save()
        return redirect('dashboard:viewuser')
    return render(request,'dashboard/update.html',{'sales':salesman})
def updatePage(request):
    return render(request,'dashboard/update.html')