from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class reg_tbl(models.Model):
    fn=models.CharField(max_length=50)
    mb=models.IntegerField()
    em=models.EmailField()
    ps=models.CharField(max_length=16)
    ps2=models.CharField(max_length=16)
class Product(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(null=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    # image=models.ImageField(upload_to='products/')
    def _str_(self):
        return self.name
    
class CartItem(models.Model):
    product=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField(default=0)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    date_added=models.DateTimeField(auto_now_add=True)
    Payment_status=models.CharField(max_length=30)
    def _str_(self):
        return f'{self.quantity} x {self.product.name}'
    
class Contact(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    message=models.TextField()
    def _str_(self):
        return self.name
    
class admin_loginpage(models.Model):
    Name=models.CharField(max_length=30)
    Password=models.CharField(max_length=30)
    def __str__(self):
        return self.Name

  
class Purchase(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    address=models.TextField()
    def __str__(self):
        return self.name




















