from django.shortcuts import render,redirect
from . models import *
from  dashboard .models import Salesman
# Create your views here.

def index(request):
    if request.method=='POST':
        userName=request.POST['username']
        passWord=request.POST['password']
        try:
            sales=Salesman.objects.get(name=userName,password=passWord)
        except Salesman.DoesNotExist:
            erroR='Invalid user name or password'
            return render(request,'pro_app/index.html',{'error':erroR})
        return redirect('dashboard:index')
    return render(request,'pro_app/index.html')