from django.urls import path
from .import views

app_name='transactions_app'

urlpatterns=[
    # path('custest',views.cusregistration,name='cusregister'),
    path('transaction',views.transacTions,name='Transaction')
]