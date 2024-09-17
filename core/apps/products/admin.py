from django.contrib import admin

from core.apps.products.models.products import ProductModel

@admin.register(ProductModel)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'description', 'created_at', 'updated_at')
