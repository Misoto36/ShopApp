from django.contrib import admin
# Register your models here.
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('name', 'description')

class CreateItemInLine(admin.TabularInline):
    model = CartItem
    extra = 0

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display =('id','total_items','total_price')
    inlines = [CreateItemInLine]
