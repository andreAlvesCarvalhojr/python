from django.contrib import admin
from .models import Products

# Register your models here.
class MonoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock')
    search_fields = ('name',)

admin.site.register(Products, MonoAdmin)
