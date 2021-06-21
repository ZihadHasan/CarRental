from django.contrib import admin
from .models import buyer, car, payment, seller, sold

# Register your models here.
admin.site.register(buyer)
admin.site.register(car)
admin.site.register(payment)
admin.site.register(seller)
admin.site.register(sold)