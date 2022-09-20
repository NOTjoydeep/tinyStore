from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from storeapp.admin import ProductAdmin, ProductImageInline
from storeapp.models import Product
from tags.models import TaggedItem
from .models import User

# Register your models here.
@admin.register(User)
class UserAdmin(BaseUserAdmin):
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "first_name", "last_name", "username", "password1", "password2"),
            },
        ),
    )


class TagInline(GenericStackedInline):
    autocomplete_fields = ['tag']
    model = TaggedItem


class CustomProductAdmin(ProductAdmin):
    inlines = [TagInline, ProductImageInline]

admin.site.unregister(Product)
admin.site.register(Product, CustomProductAdmin)

