from django.contrib import admin
from MyApp.models import *
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name',)
    

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


admin.site.register(Product,ProductAdmin)

admin.site.register(Category,CategoryAdmin)
