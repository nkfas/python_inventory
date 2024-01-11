from django.db import models

# Create your models here.
class CustomerMaster(models.Model):
    cuscode=models.TextField()
    cusname=models.TextField()
    cusemail=models.TextField()
