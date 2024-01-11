from django.db import models
from django.contrib.auth.models import User

# Create your models here.
category=(
    ('stationary','stationary'),
    ('electronics','electonics'),
    ('networks','networks')
)
class Product(models.Model):
    name = models.TextField(max_length=100,null=True)
    category = models.TextField(max_length=100,choices=category, null=True)
    price = models.FloatField(null=True)
    def __str__(self):
        return f'{self.name}--{self.price}'
    
class Order(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    staf=models.ForeignKey(User,models.CASCADE,null=True)
    orderqty=models.PositiveIntegerField(null=True)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return f'{self.product}orderd by{self.staf.username}'
    
