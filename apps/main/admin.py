from django.contrib import admin
from .models import Product, Bill, ProductImage


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class AdminProductDisplay(admin.ModelAdmin):
    readonly_fields = ('slug', 'count_bill', )
    fields = ('slug', 'title', 'desc', 'count_bill', )
    search_fields = ('title', )
    inlines = (ProductImageInline, )


@admin.register(Bill)
class AdminBillDisplay(admin.ModelAdmin):
    pass