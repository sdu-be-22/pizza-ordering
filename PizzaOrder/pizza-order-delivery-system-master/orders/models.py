from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Topping(models.Model):
	name = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5,decimal_places=2)

	def __str__(self):
		return f"with {self.name} topping"



class Veg_Pizza(models.Model):
	pizza_type = models.CharField(max_length=64)
	regular = models.DecimalField(max_digits=5, decimal_places=2)
	medium = models.DecimalField(max_digits=5, decimal_places=2)
	large = models.DecimalField(max_digits=5, decimal_places=2) 

	def __str__(self):
		return f"Selected {self.pizza_type} "

class NonVeg_Pizza(models.Model):
	pizza_type = models.CharField(max_length=64 ,  default=None)
	regular = models.DecimalField(max_digits=5, decimal_places=2)
	medium = models.DecimalField(max_digits=5, decimal_places=2)
	large = models.DecimalField(max_digits=5, decimal_places=2)


	def __str__(self):
		return f"Selected {self.pizza_type} "

class Cart(models.Model):
	item = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	extras = models.CharField(max_length=64 , null=True, blank=True)
	user = models.ManyToManyField(User , related_name="member")

class Orders(models.Model):
	item = models.CharField(max_length=64)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	extras = models.CharField(max_length=64 , null=True, blank=True)
	user = models.ManyToManyField(User , related_name="customer")





	













