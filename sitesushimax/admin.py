from django.contrib import admin
from .models import Product, ProductCategory, Order, Cart


class SushiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'discount_price', 'image', 'is_published')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description')
    prepopulated_fields = {"slug": ("name",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {"slug": ("name",)}


# Register your models here.

admin.site.register(Product, SushiAdmin)
admin.site.register(ProductCategory, CategoryAdmin)
admin.site.register(Order)
admin.site.register(Cart)
