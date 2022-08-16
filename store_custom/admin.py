from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from storeapp.admin import ProductAdmin
from storeapp.models import Product
from tags.models import TaggedItem

# Register your models here.
class TagInline(GenericStackedInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

