from django.contrib import admin

from .models import Category, SubCategory, Supplier, Product, ProductPhoto

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	exclude = ('slug', )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Supplier)
class SupplierCategoryAdmin(admin.ModelAdmin):
	pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	pass

@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
	pass

