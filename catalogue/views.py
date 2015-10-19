import json

from django import views
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404

from braces.views import LoginRequiredMixin, AjaxResponseMixin, JSONResponseMixin

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

class ProductListView(JSONResponseMixin, AjaxResponseMixin, views.generic.ListView):

	model = models.Product
	context_object_name = 'product_list'
	template_name = 'producten.html'

	# custom logic
	categories = models.Category.objects.all() # we definitely need all categories
	# suppliers = models.Supplier.objects.all() # we could use all supplier
	# subcategories = models.SubCategory.objects.all()

	
	def get_ajax(self, request, *args, **kwargs):


		'''
		context_object_name = 'category_list'
		model = models.Category
		template_name = 'subcategory-tag-buttons.html'
		'''

		print 'ajax call'

		
		selected = self.request.GET.get('selected', 'empty')
		#print selected

		self.get_suppliers_and_subcategories(selected)

		subs = self.subcategories.values_list('name', flat=True)
		sups = self.suppliers.values_list('name', flat=True)

		subcategories = []
		suppliers = []

		for sub in subs:
			subcategories.append(sub)

		for sup in sups:
			suppliers.append(sup)

		#print subcategories
		#print suppliers

		my_dict = {}

		my_dict['subcategories'] = subcategories
		my_dict['suppliers'] = suppliers

		#print my_dict

		return JsonResponse(my_dict)

	def get_context_data(self, **kwargs):

		ctx = super(ProductListView, self).get_context_data(**kwargs) # Fetch all products

		self.selected = self.request.GET.get('selected', 'empty')
		print 'categorie geselecteerd? ' + self.selected

		if self.selected != 'empty':
			self.get_suppliers_and_subcategories(self.selected)
			ctx['subcategories'] = self.subcategories

		ctx['categories'] = self.categories

		return ctx


	def get_queryset(self):
		return self.model.objects.all()



	def get_categories(self):
		return models.Category.objects.all()


	def get_suppliers_and_subcategories(self, category):

		current_category = models.Category.objects.get(name=category)

		print 'hmm? ' + current_category.name

		self.subcategories = models.SubCategory.objects.filter(parent_category=current_category)
		self.suppliers = models.Supplier.objects.filter(categories__in=self.subcategories)

		print 'aantal subs: ' + str(self.subcategories.count())

class TagsForCategoryView(AjaxResponseMixin, views.generic.ListView):

	model = models.Product
	context_object_name = 'product_list'
	#template_name = 'producten.html'
	template_name = 'products.html'


	category_name = ''
	category_tags = []
	subcategory_tags = []
	supplier_tags = []
	selection = False


	def get_queryset(self):

		self.category_name = self.request.GET.get('selected', 'empty')

		if self.category_name == 'empty':

			# Default case = ''
			self.category_name = ''
			return self.model.objects.all()

		else:
			filtered_queryset = self.model.objects.filter(subcategory__parent_category__name__iexact=self.category_name)

			if filtered_queryset.count() == 0:

				# If count = 0: doesn't exists so fallback to default case of ''
				self.category_name = ''
				return self.model.objects.all()

			else:

				print 'aantal = ' + str(filtered_queryset.count())
				self.selection = True

				return filtered_queryset
				
	def get_context_data(self, **kwargs):

		ctx = super(TagsForCategoryView, self).get_context_data(**kwargs)
		self.category_tags = list(models.Category.objects.values_list('name', flat=True))

		if self.category_name != '':

			current_category = models.Category.objects.get(name__iexact=self.category_name)

			filtered_subs = models.SubCategory.objects.filter(parent_category=current_category)

			self.subcategory_tags = list(filtered_subs.values_list('name', flat=True))
			self.supplier_tags = list(filtered_subs.values_list('suppliers__name', flat=True))

			#print 'subs: ' + str(self.subcategory_tags)
			#print 'sups: ' + str(self.supplier_tags)

		else:

			self.subcategory_tags = list(models.SubCategory.objects.values_list('name', flat=True))
			self.supplier_tags = list(models.Supplier.objects.values_list('name', flat=True))

		ctx['categories'] = self.category_tags
		ctx['subcategories'] = self.subcategory_tags
		ctx['suppliers'] = self.supplier_tags
		ctx['selection'] = self.selection

		return ctx

	def render_to_response(self, context, **response_kwargs):

		return super(TagsForCategoryView, self).render_to_response(context, **response_kwargs)


		if self.request.is_ajax():

			json_dict = {
				'suppliers': self.supplier_tags,
				'subcategories': self.subcategory_tags
			}

			print 'ajax'
			print JsonResponse(json_dict)

		else:

			print 'render to response'

			return super(TagsForCategoryView, self).render_to_response(context, **response_kwargs)



# Create your views here
class SupplierProductListView(AjaxResponseMixin, views.generic.ListView):
	'''
	Allows to show product list for given supplier in URL	
	'''

	print 'supplier product list view'

	context_object_name = 'supplier_list'
	template_name = 'modal-supplier-products.html'

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


class CategorySubCategoryListView(AjaxResponseMixin, views.generic.ListView):

	model = models.SubCategory
	context_object_name = 'subcategory-list'
	template_name = 'subcategory-tag-buttons.html'

	def get_queryset(self):

		# super(self, CategorySubCategoryListView).get_queryset()

		category_name = self.request.GET.get('selected', 'empty')
		parent = models.Category.objects.filter(name=category_name)

		print 'parent: ' + str(parent)

		filtered = self.model.objects.all()
		print 'all ' + str(filtered)

		test2 = self.model.objects.filter(parent_category=parent)

		print 'filtered:' + str(test2)

		return self.model.objects.filter(parent_category=parent)



class ProductDetailView(views.generic.DetailView):
	'''
	Shows product details
	'''

	print 'product detail open'

	model = models.Product
	template_name = 'modal_product_detail.html'





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



class TestView(JSONResponseMixin, AjaxResponseMixin, views.generic.ListView):

	model = models.SubCategory
	context_object_name = 'category_list'
	template_name = 'producten.html'
	
	def get_queryset(self):

		print self.request.GET.get('selected', 'empty')

		cat = self.request.GET.get('test', 'leeg')

		print 'name= ' + cat

		return self.model.objects.filter(name=cat)

	def get_ajax(self, request, *args, **kwargs):

		qset = self.get_queryset()
		json_dict = list(qset.values('name'))

		return self.render_json_response(json_dict)


class DentemmView(views.generic.TemplateView):

	template_name = 'product_overview.html'

class TestHomePage(views.generic.TemplateView):

	template_name = 'index_test.html'

class ServiceView(views.generic.TemplateView):

	template_name = 'services.html'
