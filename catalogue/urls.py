from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = [
    #url(r'^(?P<slug>[^/]+)/$', CategoryCreateView.as_view(), name='category_detail'),

    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),

    url(r'^suppliers/([\w-]+)/$', views.SupplierProductListView.as_view(), name='jeej'),

    url(r'^dashboard/logout/$', 'django.contrib.auth.views.logout', {'next_page': 'category-list'}, name='logout'),

    url(r'^test/(?P<slug>[\w-]+)/$', views.CategoryView.as_view(), name='test'),

    url(r'^dashboard/categorie/list/$', views.CategoryListView.as_view(), name='category-list'),
    url(r'^dashboard/categorie/new/$', views.CategoryCreateView.as_view(), name='category-new'),
    #url(r'^dashboard/categorie/list/delete/$', CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^dashboard/categorie/delete/(?P<slug>[\w-]+)/$', views.CategoryDeleteView.as_view(), name='category-delete'),
    url(r'^dashboard/categorie/update/(?P<slug>[\w-]+)/$', views.CategoryUpdateView.as_view(), name='category-update'),

    url(r'^dashboard/subcategorie/list/$', views.SubCategoryListView.as_view(), name='subcategory-list'),
    url(r'^dashboard/subcategorie/new/$', views.SubCategoryCreateView.as_view(), name='subcategory-new'),
    url(r'^dashboard/subcategorie/delete/(?P<slug>[\w-]+)/$', views.SubCategoryDeleteView.as_view(), name='subcategory-delete'),
    url(r'^dashboard/subcategorie/update/(?P<slug>[\w-]+)/$', views.SubCategoryUpdateView.as_view(), name='subcategory-update'),

    url(r'^dashboard/leverancier/list/$', views.SupplierListView.as_view(), name='supplier-list'),
    url(r'^dashboard/leverancier/new/$', views.SupplierCreateView.as_view(), name='supplier-new'),
    url(r'^dashboard/leverancier/delete/(?P<slug>[\w-]+)/$', views.SupplierDeleteView.as_view(), name='supplier-delete'),
    url(r'^dashboard/leverancier/update/(?P<slug>[\w-]+)/$', views.SupplierUpdateView.as_view(), name='supplier-update'),

    url(r'^dashboard/product/list/$', views.ProductListView.as_view(), name='product-list'),
    url(r'^dashboard/product/new/$', views.ProductCreateView.as_view(), name='product-new'),
    url(r'^dashboard/product/delete/(?P<slug>[\w-]+)/$', views.ProductDeleteView.as_view(), name='product-delete'),
    url(r'^dashboard/product/update/(?P<slug>[\w-]+)/$', views.ProductUpdateView.as_view(), name='product-update'),

    url(r'^dashboard/productafbeelding/list/$', views.ProductPhotoListView.as_view(), name='productphoto-list'),
    url(r'^dashboard/productafbeelding/new/$', views.ProductPhotoCreateView.as_view(), name='productphoto-new'),
    url(r'^dashboard/productafbeelding/delete/(?P<slug>[\w-]+)/$', views.ProductPhotoDeleteView.as_view(), name='productphoto-delete'),
    url(r'^dashboard/productafbeelding/update/(?P<slug>[\w-]+)/$', views.ProductPhotoUpdateView.as_view(), name='productphoto-update'), 


    #url(r'^category/new/$', CategoryCreateView.as_view(), name='category-new'),
    #url(r'^category/list/$', CategoryListView.as_view(), name='category-list'),
    #url(r'^category/list/delete/$', ItemDeleteView.as_view(), name='item-delete'),
    url(r'^category/(?P<slug>[\w]+)/$', views.CategoryDetailView.as_view(), name='category-detail'),
    #url(r'^category/delete/(?P<slug>[\w-]+)/$', CategoryDeleteView.as_view(), name='category-delete'),
    #url(r'^category/update/(?P<slug>[\w-]+)/$', CategoryUpdateView.as_view(), name='category-update'),

    #url(r'^subcategory/new$', SubCategoryCreateView.as_view(), name='subcategory-new'),

    url(r'^supplier/new$', views.SupplierCreateView.as_view(), name='supplier-new'),
    url(r'^supplier/update/(?P<slug>[\w-]+)/$', views.SupplierUpdateView.as_view(), name='supplier-update'),

    url(r'^dashboard/user/list/$', views.UserListView.as_view(), name='user-list'),

    url(r'^temm/(?P<slug>[\w-]+)$', views.ProductDetailView.as_view(), name='user-detail'),
]
