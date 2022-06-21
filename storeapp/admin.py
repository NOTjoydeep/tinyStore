from django.contrib import admin
from django.db.models.aggregates import Count
from django.utils.html import format_html, urlencode
from django.urls import reverse
from . import models

# Register your models here.

# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['title', 'unit_price']

# admin.site.register(models.Product, ProductAdmin)

@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price', 'inventory_status', 'collection_title']
    list_editable = ['unit_price']
    list_per_page = 10
    list_select_related = ['collection']

    def collection_title(self, product):
        return product.collection.title

    @admin.display(ordering='inventory')
    def inventory_status(self, product):
        if product.inventory == 0:
            return 'EMPTY' + ' (' + str(product.inventory) + ')'
        elif product.inventory < 10:
            return 'VERY LOW' + ' (' + str(product.inventory) + ')'
        elif product.inventory < 20:
            return 'LOW' + ' (' + str(product.inventory) + ')'
        else:
            return 'OK' + ' (' + str(product.inventory) + ')'
    
    # ordering = ['title', 'inventory_status']

@admin.register(models.Collection)
class CollectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'product_count']

    # @admin.display(ordering='product_count')
    # def product_count(self, collection):
    #     return collection.product_count

    @admin.display(ordering='product_count')
    def product_count(self, collection):
        # reverse('admin:app_model_page')
        url = (
            reverse('admin:storeapp_product_changelist')
            + '?'
            + urlencode({
                'collection_id': str(collection.id)
            })
        )
        # print(url)
        return format_html('<a href="{}">{}</a>', url, collection.product_count)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            product_count = Count('product')
        )

@admin.register(models.Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'placed_at', 'customer']
    list_per_page = 10
    ordering = ['id', 'placed_at', 'customer']

    # def customer(self, order):
    #     return order.customer


