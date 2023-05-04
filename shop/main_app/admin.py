from django.contrib import admin
from main_app.models import CustomUser, Product, Purchase, Return


# Register your models here.

admin.site.register(CustomUser)
admin.site.register(Product)
admin.site.register(Purchase)
admin.site.register(Return)


