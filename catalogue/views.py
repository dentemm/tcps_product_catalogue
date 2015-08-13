from django.shortcuts import render
from django.contrib import messages
from django.views.generic import CreateView, DeleteView, UpdateView, DetailView, ListView, TemplateView
from django.core.urlresolvers import reverse_lazy
from django.http import JsonResponse

from .models import *


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
		ctx['modelname'] = subcategorie
		return ctx

class SupplierActionMixin(object):
	fields = ['name', 'slug', 'description', 'website', 'logo']

	def get_context_data(self, **kwargs):
		ctx = super(SupplierActionMixin, self).get_context_data(**kwargs)
		ctx['modelname'] = supplier
		return ctx


class AjaxResponseMixin(object):
    """
    Mixin allows you to define alternative methods for ajax requests. Similar
    to the normal get, post, and put methods, you can use get_ajax, post_ajax,
    and put_ajax.
    """
    def dispatch(self, request, *args, **kwargs):
        request_method = request.method.lower()

        if request.is_ajax() and request_method in self.http_method_names:
            handler = getattr(self, "{0}_ajax".format(request_method),
                              self.http_method_not_allowed)
            self.request = request
            self.args = args
            self.kwargs = kwargs
            return handler(request, *args, **kwargs)

        return super(AjaxResponseMixin, self).dispatch(
            request, *args, **kwargs)

    def get_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def post_ajax(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def put_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

    def delete_ajax(self, request, *args, **kwargs):
        return self.get(request, *args, **kwargs)

class AjaxableResponseMixin(object):
	'''
	Allow our forms to support ajax calls as well
	'''

	print 'in ajax call'

	def form_invalid(self, form):

		response = super(AjaxableResponseMixin, self).form_invalid(form)

		if self.request.is_ajax():
			return JsonResponse(form.errors, status=400)

		else:
			return response

	def form_valid(self, form):

		response = super(AjaxableResponseMixin, self).form_valid(form)

		if self.request.is_ajax():
			data = {
				'pk': self.object.pk,
			}
			return JsonResponse(data)

		else:
			return response


class SubCategoryActionMixin(object):
	fields = ['name', 'slug', 'description', 'parent_category', 'suppliers']



class DashboardView(TemplateView):
	template_name = 'dashboard_home.html'


#Category views
class CategoryDetailView(DetailView):

	model = Category
	template_name = 'category_detail.html'

class CategoryListView(ListView):

	print 'category list view'

	model = Category
	context_object_name = 'item_list'
	template_name = 'item_list.html'

	def get_queryset(self):
		return Category.objects.all()

	def get_context_data(self, **kwargs):
		ctx = super(CategoryListView, self).get_context_data(**kwargs)
		ctx['modelname'] = 'categorie'
		return ctx

class CategoryCreateView(CategoryActionMixin, CreateView):

	model = Category
	template_name = 'item_edit.html'
	success_url = reverse_lazy('category-list')

	'''
	def get_context_data(self, **kwargs):
		ctx = super(CategoryCreateView, self).get_context_data(**kwargs)
		ctx['modelname'] = 'category'
		return ctx
	'''


class CategoryUpdateView(CategoryActionMixin, UpdateView):

	model = Category
	template_name = 'item_edit.html'
	success_url = reverse_lazy('category-list')


class CategoryDeleteView(AjaxResponseMixin, DeleteView):

	model = Category
	success_url = reverse_lazy('category-list')
	template_name = 'item_delete.html'

	def post_ajax(self, request, *args, **kwargs):
		print 'ajax great succes!'

	def post(self, request, *args, **kwargs):
		print 'great succes!'

	def delete_ajax(self, request, *args, **kwargs):
		print 'ajax delete CategoryDeleteView'

		self.object = self.get_object()
		self.object.delete()
		payload = {'delete': 'ok'}
		return JsonResponse(payload)

	def dispatch(self, *args, **kwargs): #View part of view: accepteert request en retourneert response

		self.slug = kwargs['slug']
		return super(CategoryDeleteView, self).dispatch(*args, **kwargs)

#Subcategorie views
class SubCategoryListView(ListView):

	model = SubCategory
	context_object_name = 'item_list'
	template_name = 'item_list.html'

	def get_queryset(self):
		return SubCategory.objects.all()

	def get_context_data(self, **kwargs):
		ctx = super(SubCategoryListView, self).get_context_data(**kwargs)
		ctx['modelname'] = 'subcategorie'
		return ctx

class SubCategoryCreateView(SubCategoryActionMixin, CreateView):

	model = SubCategory
	template_name = 'item_edit.html'
	success_url = reverse_lazy('subcategory-list')


class SubCategoryUpdateView(SubCategoryActionMixin, UpdateView):

	model = SubCategory
	template_name = 'item_edit.html'
	success_url = reverse_lazy('subcategory-list')

class SubCategoryDeleteView(AjaxResponseMixin, DeleteView):

	model = SubCategory
	success_url = reverse_lazy('subcategory-list')
	template_name = 'item_delete.html'

	def delete_ajax(self, request, *args, **kwargs):
		print 'ajax delete SubCategoryDeleteView'

		self.object = self.get_object()
		self.object.delete()
		payload = {'delete': 'ok'}
		return JsonResponse(payload)

	def dispatch(self, *args, **kwargs): #View part of view: accepteert request en retourneert response

		self.slug = kwargs['slug']
		return super(SubCategoryDeleteView, self).dispatch(*args, **kwargs)


#Supplier views
class SupplierListView(ListView):

	model = Supplier
	context_object_name = 'item_list'
	template_name = 'item_list.html'

	def get_queryset(self):
		return Supplier.objects.all()

	def get_context_data(self, **kwargs):
		ctx = super(SupplierListView, self).get_context_data(**kwargs)
		ctx['modelname'] = 'leverancier'
		return ctx

class SupplierCreateView(SupplierActionMixin, CreateView):

	model = Supplier
	template_name = 'item_edit.html'

class SupplierUpdateView(SupplierActionMixin, UpdateView):

	model = Supplier
	template_name = 'item_edit.html'

class SupplierDeleteView(AjaxResponseMixin, DeleteView):

	model = Supplier
	success_url = reverse_lazy('supplier-list')
	template_name = 'item_delete.html'

	def delete_ajax(self, request, *args, **kwargs):
		print 'ajax delete SupplierDeleteView'

		self.object = self.get_object()
		self.object.delete()
		payload = {'delete': 'ok'}
		return JsonResponse(payload)

	def dispatch(self, *args, **kwargs): #View part of view: accepteert request en retourneert response

		self.slug = kwargs['slug']
		return super(SubCategoryDeleteView, self).dispatch(*args, **kwargs)


class ItemDeleteView(AjaxResponseMixin, DeleteView):

	model = Category
	success_url = reverse_lazy('category-list')
	template_name = 'item_delete.html'

	def dispatch(self, *args, **kwargs): 
		self.item_id = kwargs['pk'] 
		print self.item_id
		return super(ItemUpdateView, self).dispatch(*args, **kwargs)

	def post(self, request, *args, **kwargs):
		print 'great succes!'

	def post_ajax(self, request, *args, **kwargs):
		print 'ajax great succes!'

		reponse = JsonResponse({'foo': 'bar'})

		print 'error?'

		return response

	def delete_ajax(self, request, *args, **kwargs):

		self.object = self.get_object()

		print 'delete ajax'
		print self.object
		print 'test'


class SubCategoryDetailView(DetailView):

	model = SubCategory



