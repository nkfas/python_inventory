from django.shortcuts import render


# Create your views here.
def transacTions(request):
    return render(request,'transaction_app\sales.html')


