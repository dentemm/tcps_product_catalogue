from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = [
    #url(r'^(?P<slug>[^/]+)/$', CategoryCreateView.as_view(), name='category_detail'),

    url(r'^overview/$', views.TestProductOverviewPage.as_view(), name='product-overview'),
    url(r'^overview/suppliers/$', views.SupplierOverviewPage.as_view(), name='supplier-product-overview'),

    url(r'^overview/products/$', views.ProductListView.as_view(), name='products-list'),

    url(r'^test/tim/$', views.CategorySubCategoryListView.as_view(), name='testview'),


    url(r'^category/(?P<category>[\w-]+)/$', views.CategorySubCategoryListView.as_view(), name='category-subcategory-list'),
    url(r'^suppliers/(?P<supplier>[\w-]+)/$', views.SupplierProductListView.as_view(), name='supplier-product-list'),
    url(r'^subcategory/(?P<subcategory>[\w-]+)/$', views.SubcategoryProductListView.as_view(), name='subcategory-product-list'),

    url(r'^category/(?P<slug>[\w]+)/$', views.CategoryDetailView.as_view(), name='category-detail'),


    #url(r'^test/overview/$', views.TestProductOverviewPage.as_view(), name='product-overview'),

    # Overview page, and only main view for this application
    url(r'^overview/all/$', views.TagsForCategoryView.as_view(), name='tagview'),

    url(r'^services/$', views.ServiceView.as_view(), name='services'),




    url(r'^product/(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name='product-detail'),

    url(r'^dentemm/$', views.DentemmView.as_view(), name='dentemm'),
    url(r'^index/$', views.TestHomePage.as_view(), name='index-test'),
]
