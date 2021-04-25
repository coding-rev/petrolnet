from django.urls import path
from .views import *
app_name = 'mobile_app'

urlpatterns = [
	path('', index, name='index'),
	path('checkout', checkout, name='checkout'),
	path('success', success, name='success'),
	path('base', base, name='base'),
	path('purchase-petrol', buyPetrol, name='buy-petrol')
]