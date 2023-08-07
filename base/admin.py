from django.contrib import admin
from .models import FgMenuCategory, FgMenuItem, FgMenuSubCategory

# Register your models here.
admin.site.register(FgMenuCategory)
admin.site.register(FgMenuItem)
admin.site.register(FgMenuSubCategory)
