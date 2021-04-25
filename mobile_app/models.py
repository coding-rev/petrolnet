from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class FuelOrders(models.Model):
	customer 		= models.ForeignKey(User, on_delete=models.CASCADE)
	quantity 		= models.PositiveIntegerField()
	price			= models.IntegerField()
	date_ordered 	= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.customer.username

	class Meta:
		verbose_name_plural = 'Fuel Orders'

class FinalOrder(models.Model):
	name 		= models.CharField(max_length=100)
	customer 	= models.ForeignKey(User, on_delete=models.CASCADE)
	order 		= models.ForeignKey(FuelOrders, on_delete=models.CASCADE)
	phone 		= models.CharField(max_length=100)
	email 		= models.EmailField()
	comment		= models.CharField(max_length=700)
	town 		= models.CharField(max_length=100)
	paid 		= models.BooleanField(default=False)
	def __str__(self):
		return self.name

	class Meta:
		verbose_name_plural = 'Final Order'
