from django.contrib import admin
from .models import Topping, Veg_Pizza , NonVeg_Pizza , Cart , Orders
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(Topping)
admin.site.register(Veg_Pizza)
admin.site.register(NonVeg_Pizza)
admin.site.register(Cart)
admin.site.register(Orders)