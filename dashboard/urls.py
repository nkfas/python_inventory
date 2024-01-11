from django.urls import path
from .import views
app_name='dashboard'
urlpatterns =[
    path('',views.index,name='index'),
    path('Registratoin',views.Registration,name='Registration'),
    path('viewuser',views.viewuser,name='viewuser'),
    path('useractive/<int:sid>',views.UserActive,name='user_accept'),
    path('userdelete/<int:sid>',views.UserDelete,name='user_delete'),
    path('update/<int:sid>',views.updateuser,name='user_update'),
    path('updatesales',views.updatePage,name='UpdateSalem')

    
]