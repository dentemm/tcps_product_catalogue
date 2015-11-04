from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns

from . import views

urlpatterns = [

	url(r'^$', views.TagsForCategoryView.as_view(), name='products'),

    # Modal view as detail view for a product
    url(r'^product/(?P<slug>[\w-]+)/$', views.ProductDetailView.as_view(), name='product-detail'),
]
