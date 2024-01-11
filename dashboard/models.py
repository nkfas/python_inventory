from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Salesman(models.Model):
    name=models.TextField(max_length=100,null=True)
    password=models.TextField(max_length=50,null=True)
    emailaddress=models.TextField(max_length=100,null=True)
    mobileno=models.TextField(max_length=25,null=True)
    active=models.PositiveIntegerField(null=True)
    class Meta:
        db_table='registratoin'
    