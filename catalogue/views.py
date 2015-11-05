import json

from django import views
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers

from braces.views import LoginRequiredMixin, AjaxResponseMixin

from . import models

class TagsForCategoryView(AjaxResponseMixin, views.generic.ListView):
	'''
	Overview page for products, uses TagSort library which explains name
	'''

	model = models.Product
	context_object_name = 'product_list'

	category_slug = ''
	category_tags = []
	subcategory_tags = []
	supplier_tags = []
	selection = False

	def get_template_names(self):

		if self.request.is_ajax():
			self.template_name = 'product-list-content.html'

		else:
			self.template_name = 'products.html'

		#print 'template name: ' + self.template_name

		return super(TagsForCategoryView, self).get_template_names()

	def get_queryset(self):

		self.category_slug = self.request.GET.get('selected', 'empty')

		print 'get_queryset slug: ' + self.category_slug

		if self.category_slug == 'empty':

			self.category_slug = ''
			return self.model.objects.all()

		else:
			filtered_queryset = self.model.objects.filter(subcategory__parent_category__slug__iexact=self.category_slug)

			if filtered_queryset.count() == 0:
				self.category_slug = ''
				return self.model.objects.all()

			else:
				self.selection = True
				return filtered_queryset
				
	def get_context_data(self, **kwargs):

		print 'slug= ' + self.category_slug

		ctx = super(TagsForCategoryView, self).get_context_data(**kwargs)
		self.category_tags = models.Category.objects.all()

		print 'aantal tags: ' + str(self.category_tags.count())

		if self.category_slug != '':

			current_category = models.Category.objects.get(slug__iexact=self.category_slug)
			filtered_subs = models.SubCategory.objects.filter(parent_category=current_category)

			self.subcategory_tags = list(filtered_subs.values_list('name', flat=True))
			self.supplier_tags = list(filtered_subs.values_list('suppliers__name', flat=True))

		else:

			self.subcategory_tags = list(models.SubCategory.objects.values_list('name', flat=True))
			self.supplier_tags = list(models.Supplier.objects.values_list('name', flat=True))

		ctx['categories'] = self.category_tags
		ctx['subcategories'] = self.subcategory_tags
		ctx['suppliers'] = self.supplier_tags
		ctx['selection'] = self.selection

		return ctx

class ProductDetailView(views.generic.DetailView):
	'''
	Shows product details
	'''

	#print 'product detail open'

	model = models.Product
	template_name = 'modal_product_detail.html'

