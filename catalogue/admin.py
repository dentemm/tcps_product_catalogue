from django.contrib import admin

from .models import Category, SubCategory, Supplier, Product, ProductPhoto

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	exclude = ('slug', )

@admin.register(SubCategory)
class SubCategoryAdmin(admin.ModelAdmin):
	exclude = ('slug', )

@admin.register(Supplier)
class SupplierCategoryAdmin(admin.ModelAdmin):
	exclude = ('slug', )

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
	#exclude = ('slug', )
	pass

@admin.register(ProductPhoto)
class ProductPhotoAdmin(admin.ModelAdmin):
	pass

