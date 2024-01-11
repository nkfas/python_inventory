from django.urls import path
from .import views

app_name='masters'

urlpatterns=[
    # path('custest',views.cusregistration,name='cusregister'),
    path('cusregistration',views.cusregistration,name='cusRegistation')
]