from django.contrib import admin
from .models import FuelOrders, FinalOrder
# Register your models here.

admin.site.site_header = "Petrol Net"
admin.site.site_title  = "Petrol Net"

class FinalOrderAdmin(admin.ModelAdmin):
    list_display = ['customer', 'phone','order', 'town', 'paid']
    list_filter = ['paid', 'customer']

admin.site.register(FuelOrders)
admin.site.register(FinalOrder, FinalOrderAdmin)


