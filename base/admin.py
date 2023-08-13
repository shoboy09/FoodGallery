from django.contrib import admin
from .models import FgMenuCategory, FgMenuItem, FgMenuSubCategory, Reservation

# Register your models here.
admin.site.register(FgMenuCategory)
admin.site.register(FgMenuItem)
admin.site.register(FgMenuSubCategory)
admin.site.register(Reservation)