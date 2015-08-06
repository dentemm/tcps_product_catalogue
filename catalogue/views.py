from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy

from .models import *


# Create your views here.

class CategoryActionMixin(object):

	fields = ['name', 'slug', 'image']

	'''@property
	def success_msg(self):
		return NotImplemented

	def form_valid(self, form):
		messages.info(self.request, self.success_msg)
		return super(CategoryActionMixin, self).form_valid(form)'''

class SubCategoryActionMixin(object):
	fields = ['name', 'description', 'parent_category', 'suppliers']

class SupplierActionMixin(object):
	fields = ['name', 'description', 'website', 'logo']

class DashboardView(TemplateView):
	template_name = 'dashboard_home.html'


#Category views
class CategoryDetailView(DetailView):

	model = Category
	template_name = 'category_detail.html'

class CategoryListView(ListView):

	model = Category
	context_object_name = 'item_list'
	template_name = 'category_list.html'

	def get_queryset(self):

		print 'test'
		return Category.objects.all()

class CategoryCreateView(CategoryActionMixin, CreateView):

	model = Category
	template_name = 'category_edit.html'

	success_url = reverse_lazy('category-list')


	def get_context_data(self, **kwargs):
		ctx = super(CategoryCreateView, self).get_context_data(**kwargs)
		ctx['modelname'] = 'category'
		return ctx


class CategoryUpdateView(CategoryActionMixin, UpdateView):

	model = Category
	template_name = 'category_edit.html'

	success_url = reverse_lazy('category-list')


class CategoryDeleteView(DeleteView):

	model = Category
	success_url = reverse_lazy('category-list')

	template_name = 'category_delete.html'

	def dispatch(self, *args, **kwargs): #View part of view: accepteert request en retourneert response

		self.slug = kwargs['slug']
		return super(CategoryDeleteView, self).dispatch(*args, **kwargs)



class SubCategoryDetailView(DetailView):

	model = SubCategory

class SubCategoryListView(ListView):

	model = SubCategory

class SubCategoryCreateView(SubCategoryActionMixin, CreateView):

	model = SubCategory

	template_name = 'subcategory_edit.html'


class SupplierCreateView(SupplierActionMixin, CreateView):

	model = Supplier

	template_name = 'supplier_edit.html'

class SupplierUpdateView(SupplierActionMixin, UpdateView):

	model = Category

	template_name = 'supplier_edit.html'

