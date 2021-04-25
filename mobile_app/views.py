from django.shortcuts import render, redirect
from .models import FuelOrders, FinalOrder
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def base(request):
	return render(request, 'base.html')

def index(request):
	return render(request, 'index.html')

@login_required
def buyPetrol(request):
	if request.method == 'POST':
		customer 		= request.user
		quantity 		= request.POST.get('quantity')
		# Price of petrol/litre in cedi = 5.644
		price 			= int(quantity) * 5.644
		
		#Checking if the user has a saved order
		delete_old_order = FuelOrders.objects.filter(customer=customer).delete()
		order 	= FuelOrders.objects.create(customer=customer, quantity=quantity, price=price)
		messages.success(request, 'Order request saved!. Fill the form to confirm your order')
		return redirect('mobile_app:checkout')	
	return redirect('checkout')


@login_required
def checkout(request):
	user 			= request.user
	order 			= FuelOrders.objects.get(customer=user)
	order_total 	= order.price
	order_quantity	= order.quantity
	if request.method == 'POST':
		customer 		= request.user
		order 			= order
		phone 			= request.POST.get('phone')
		email 			= request.POST.get('email')
		comment 		= request.POST.get('comment')
		name 			= request.POST.get('name')
		town 			= request.POST.get('town')

		#Saving Final Order
		final_order 	= FinalOrder.objects.create(customer=customer, order=order, phone=phone,
													email=email, comment=comment, name=name, town=town)
		
		return redirect('mobile_app:success')
	context = {
		"order_total":order_total,
		"order_quantity":order_quantity
	}
	return render(request, 'checkout.html', context)

@login_required
def success(request):
	user 		= request.user
	order 		= FuelOrders.objects.get(customer=user)
	order_total = order.price
	order_quantity	= order.quantity
	context = {
	 "order_total":order_total,
	 "order_quantity":order_quantity
	}
	return render(request, 'success.html', context)



