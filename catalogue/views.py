from django import views
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from . import models

class TestProductOverviewPage(views.generic.ListView):

	print 'in TestProductOverviewPage klasse'

	model = models.Category
	context_object_name = 'category_list'
	template_name = 'producten.html'
	
	def get_queryset(self):
		return self.model.objects.all()

class SupplierOverviewPage(views.generic.ListView):

	model = models.Supplier
	context_object_name = 'supplier_list'
	template_name = 'supplier-products.html'

	def get_queryset(self):
		return self.model.objects.all()

# Create your views here
class SupplierProductListView(AjaxResponseMixin, views.generic.ListView):
	'''
	Allows to show product list for given supplier in URL	
	'''

	context_object_name = 'supplier_list'
	template_name = 'item_list.html'

	def get_queryset(self):

		supplier = self.kwargs['supplier']

		self.supplier = get_object_or_404(models.Supplier, slug=supplier)
		return models.Product.objects.filter(supplier=self.supplier)

		#self.supplier = get_object_or_404(models.Supplier, slug=self.args[0])
		#return models.Product.objects.filter(supplier=self.supplier)

class SubcategoryProductListView(AjaxResponseMixin, views.generic.ListView):
	'''
	Allows to show product list for given subcategory in URL
	'''

	#print 'subcategory product list view'

	context_object_name = 'product_list'
	template_name = 'modal_subcategory_products.html'

	'''def get_context_data(self, **kwargs):

		context = super(SubcategoryProductListView, self).get_context_data(**kwargs)
		context['subcategory'] = self.subcategory.name'''

	def get_queryset(self):

		#print 'get queryset'

		subcategory = self.kwargs['subcategory']

		self.subcategory = get_object_or_404(models.SubCategory, slug=subcategory)
		return models.Product.objects.filter(subcategory=self.subcategory)


class ProductDetailView(views.generic.DetailView):
	'''
	Shows product details
	'''

	model = models.Product
	template_name = 'product_detail.html'

class CategorySubCategoryListView(views.generic.ListView):
	'''
	Allows to show subcategory list for given category in URL
	'''

	context_object_name = 'item_list'
	template_name = 'item_list.html'

	def get_queryset(self):

		category = self.kwargs['category']

		self.category = get_object_or_404(models.Category, slug=category)
		return models.SubCategory.objects.filter(parent_category=self.category)


def logout_view(request):
    logout(request)


# Create your views here.
class CategoryActionMixin(object):

	fields = ['name', 'slug', 'image']

	def get_context_data(self, **kwargs):
		ctx = super(CategoryActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = 'categorie'
		return ctx

class SubCategoryActionMixin(object):
	
	fields = ['name', 'description', 'parent_category', 'suppliers']

	def get_context_data(self, **kwargs):
		ctx = super(SubCategoryActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = 'subcategorie'
		return ctx

class SupplierActionMixin(object):

	fields = ['name', 'slug', 'description', 'website', 'logo']

	def get_context_data(self, **kwargs):
		ctx = super(SupplierActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = 'supplier'
		return ctx

class ProductActionMixin(object):

	fields = ['name', 'product_code', 'description', 'supplier', 'subcategory', 'product_folder', 'user_manual']

	def get_context_data(self, **kwargs):
		ctx = super(ProductActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = 'product'
		return ctx

class ProductPhotoActionMixin(object):

	fields = ['image', 'product', 'alt_text', 'display_order']

	def get_context_data(self, **kwargs):
		ctx = super(ProductPhotoActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = 'productphoto'
		return ctx

class UserActionMixin(object):

	fields = ['name', 'product_code', 'description', 'supplier', 'subcategory', 'product_folder', 'user_manual']

	def get_context_data(self, **kwargs):
		ctx = super(UserActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = 'user'
		return ctx


#Category views
class CategoryDetailView(views.generic.DetailView):

	model = models.Category
	template_name = 'category_detail.html'

class CategoryListView(LoginRequiredMixin, views.generic.ListView):

	#print 'category list view'

	model = models.Category
	context_object_name = 'item_list'
	template_name = 'item_list.html'

	def get_queryset(self):
		return Category.objects.all()

	def get_context_data(self, **kwargs):
		ctx = super(CategoryListView, self).get_context_data(**kwargs)
		ctx['modelname'] = 'categorie'
		return ctx

class CategoryCreateView(CategoryActionMixin, views.generic.CreateView):

	model = models.Category
	template_name = 'item_edit.html'
	success_url = reverse_lazy('category-list')

class CategoryUpdateView(CategoryActionMixin, views.generic.UpdateView):

	model = models.Category
	template_name = 'item_edit.html'
	success_url = reverse_lazy('category-list')


class CategoryDeleteView(AjaxResponseMixin, views.generic.DeleteView):

	model = models.Category
	success_url = reverse_lazy('category-list')
	template_name = 'item_delete.html'

	def delete_ajax(self, request, *args, **kwargs):
		#print 'ajax delete CategoryDeleteView'

		self.object = self.get_object()
		self.object.delete()
		payload = {'delete': 'ok'}
		return JsonResponse(payload)

	def dispatch(self, *args, **kwargs): #View part of view: accepteert request en retourneert response

		self.slug = kwargs['slug']
		return super(CategoryDeleteView, self).dispatch(*args, **kwargs)





