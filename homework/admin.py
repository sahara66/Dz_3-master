from django.contrib import admin
from.models import (Category, Product, Review)

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'price']
    search_fields = ['title']
    list_filter = ['title']
    list_editable = ['price', 'title']
    list_per_page = 1

admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
admin.site.register(Review)


