from django.contrib import admin

from .models import Category, SubCategory, Supplier, Product, ProductPhoto

# Register your models here.
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(ProductPhoto)