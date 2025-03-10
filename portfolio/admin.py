from django.contrib import admin
from .models import Tab, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'year', 'sector', 'category', 'url', 'image_url', 'description', 'tab')

admin.site.register(Tab)
admin.site.register(Product, ProductAdmin)
