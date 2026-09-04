from django.contrib import admin
from . models import Product,OfferingDiscount


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","stock")


class OfferingDiscountAdmin(admin.ModelAdmin):
    list_display = ("code","discount")


admin.site.register(Product,ProductAdmin)
admin.site.register(OfferingDiscount,OfferingDiscountAdmin)