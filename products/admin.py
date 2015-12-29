# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Product
from .models import Company
from .models import Units
from .models import Type


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                {'fields':['image', 'type', 'company', 'units', 'cost']}),
        ('Tobacco',           {'fields':['flower', 'weight_tobacco'],'classes': ['collapse']}),
        ('Waterpipe',         {'fields':['model', 'height_shisha', 'type_bowls'],'classes': ['collapse']}),
        (None,                {'fields':['characteristics', 'specification']}),
    ]
    list_display = ('type', 'flower', 'model')
    list_filter = ['type']
    search_fields = ['flower','type', 'model']
admin.site.register(Product, ProductAdmin)
admin.site.register(Company)
admin.site.register(Units)
admin.site.register(Type)
# Register your models here.
