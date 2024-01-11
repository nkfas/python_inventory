from django.shortcuts import render,redirect
from .forms import CustomerForm

# Create your views here.
# def cusregistration(request):
#     if request.method=='POST':
#         form=CustomerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('masters:cusregister')
#     else :
#         form=CustomerForm
#     return render(request,'masters/customermaster.html',{'form':form})

def cusregistration(request):
    return render(request,'masters\cusregistration.html')
