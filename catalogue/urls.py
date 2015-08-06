from django.conf.urls import url

from .views import *

urlpatterns = [
    #url(r'^(?P<slug>[^/]+)/$', CategoryCreateView.as_view(), name='category_detail'),

    url(r'^dashboard/$', DashboardView.as_view(), name='dashboard'),

    url(r'^category/new/$', CategoryCreateView.as_view(), name='category-new'),
    url(r'^category/list/$', CategoryListView.as_view(), name='category-list'),
    url(r'^category/(?P<slug>[\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^category/delete/(?P<slug>[\w-]+)/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^category/update/(?P<slug>[\w-]+)/$', CategoryUpdateView.as_view(), name='category-update'),

    url(r'^subcategory/new$', SubCategoryCreateView.as_view(), name='subcategory-new'),

    url(r'^supplier/new$', SupplierCreateView.as_view(), name='supplier-new'),
    url(r'^supplier/update/(?P<slug>[\w-]+)/$', SupplierUpdateView.as_view(), name='supplier-update'),

]