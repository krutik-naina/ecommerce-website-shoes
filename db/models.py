from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Customer (models.Model):
	ename = models.CharField(max_length=30)
	email = models.CharField(max_length=30)
	epassword = models.CharField(max_length=30)

class Product (models.Model):
	img = models.FileField(upload_to='upload/', max_length=250, null=True, default=None)
	products = models.CharField(max_length=30)
	price = models.DecimalField(max_digits=10, decimal_places=2)
	
	def __str__(self):
		return self.products


class CartItem (models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
	    return f'{self.quantity} x {self.product.products}'


class Contacts (models.Model):
	cname = models.CharField(max_length=30)
	cemail = models.CharField(max_length=30)
	ccomment = models.CharField(max_length=100)
