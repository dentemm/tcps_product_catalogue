# -*- coding: utf-8 -*-

from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse_lazy, reverse

# Create your models here.
class MetaOptionsMixin(object):

 	def get_verbose_name(self):
 		return self._meta.verbose_name

  	def get_verbose_name_plural(self):
 		return self._meta.verbose_name_plural

	def get_class_name(self):
		return self._meta.object_name

class Category(MetaOptionsMixin, models.Model):

	name = models.CharField(_('naam'), max_length=255, blank=False, unique=True)
	slug = models.SlugField(_('slug'), unique=True, blank=True, max_length=255)
	image = models.ImageField(_('afbeelding'), upload_to='category/images', blank=True, null=True)
	icon = models.ImageField(_('icoontje'), upload_to='category/icons', blank=True, null=True)
	# description = models.TextField(_('Description'), null=True, blank=True) //Provided by django cms

	class Meta:
		app_label = 'catalogue'
		ordering = ['name']
		verbose_name = _('categorie')
		verbose_name_plural = _('categorieen')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):

		if not self.id:
			self.slug = slugify(self.name)

		super(Category, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return '/dashboard/' 

class SubCategory(MetaOptionsMixin, models.Model):

	name = models.CharField(_('naam'), max_length=255, unique=True)
	slug = models.SlugField(_('slug'), blank=True, unique=True)
	parent_category = models.ForeignKey('Category', verbose_name=_('categorie'), related_name='subcategories')
	suppliers = models.ManyToManyField('Supplier', verbose_name=_('leverancier'), related_name='categories')
	image = models.ImageField(_('afbeelding'), upload_to='subcategory/images', blank=True, null=True)
	# description = models.TextField(_('beschrijving'), null=True, blank=True) //Provided by django cms

	class Meta:
		app_label = 'catalogue'
		ordering = ['name']
		verbose_name = _('subcategorie')
		verbose_name_plural = _('subcategorieen')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):

		if not self.id:
			self.slug = slugify(self.name)

		super(SubCategory, self).save(*args, **kwargs)

	def get_ancestor_and_self(self):
		return [self.parent_category.slug, self.slug]


class Supplier(MetaOptionsMixin, models.Model):

	name = models.CharField(_('naam'), max_length=255, unique=True)
	slug = models.SlugField(_('slug'), blank=True, unique=True)
	website = models.URLField(_('link naar website'), blank=True)
	logo = models.ImageField(_('logo'), upload_to='supplier/logo', max_length=255, blank=True)
	#description = models.TextField(_('beschrijving'), null=True, blank=True) //Provided by django cms

	class Meta:
		app_label = 'catalogue'
		ordering = ['name']
		verbose_name = _('leverancier')
		verbose_name_plural = _('leveranciers')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):

		if not self.id:
			self.slug = slugify(self.name)

		super(Supplier, self).save(*args, **kwargs)

class Product(MetaOptionsMixin, models.Model):

	name = models.CharField(_('naam'), max_length=255)
	slug = models.SlugField(_('slug'), blank=True, unique=False)
	product_code = models.CharField(_('product code'), max_length=128, blank=True, unique=True)
	supplier = models.ForeignKey(Supplier, verbose_name='leverancier', related_name='products')
	subcategory = models.ForeignKey(SubCategory, verbose_name='subcategorie', related_name='products')
	product_folder = models.FileField(_('product folder'), upload_to='product/documentation', null=True, blank=True)
	user_manual = models.FileField(_('manual'), upload_to='product/documentation', null=True, blank=True)
	# description = models.TextField(_('beschrijving'), null=True, blank=True) //Provided by django cmss

	_slug_separator = '/'
	_category_separator = ' - '

	class Meta:

		app_label = 'catalogue'
		verbose_name = _('product')
		verbose_name_plural = _('producten')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		#return reverse_lazy('product-list') #test
		return reverse('product-detail', kwargs={'slug':self.slug})

	def save(self, *args, **kwargs):

		if not self.id:
			self.slug = slugify(self.name)

		super(Product, self).save(*args, **kwargs)

	def get_full_slug(self):
		slugs = self.subcategory.get_ancestor_and_self() + [self.slug]
		return self._slug_separator.join(slugs)

	def get_category_subcategory(self):
		'''
		Returns: <Category - SubCategory> (first letters uppercased)
		'''
		return (self.subcategory.parent_category.name + self._category_separator + self.subcategory.name).title()

	def get_supplier_name(self):

		return self.supplier.name

	def get_subcategory_name(self):

		return self.subcategory.name



class ProductPhoto(MetaOptionsMixin, models.Model):

	image = models.ImageField(_('foto'), upload_to='product/photos', max_length=255)
	alt_text = models.CharField(_('korte beschrijving'), max_length=255, null=True, blank=True)
	product = models.ForeignKey(Product, verbose_name=_('product'), related_name='images')
	display_order = models.PositiveIntegerField(_('weergave volgorde'), default=0, unique=True)
	date_created = models.DateTimeField(_('datum toegevoegd'), auto_now_add=True)

	class Meta:

		app_label = 'catalogue'
		verbose_name = _('product afbeelding')
		verbose_name_plural = _('product afbeeldingen')

	def __string__(self):

		return "Afbeelding %s van %s" % (self.display_order + 1, self.product)

	def __unicode__(self):
		return "Afbeelding %s van %s" % (self.display_order + 1, self.product)

	def is_primary(self):
		'''
		Return true if display order is 0, else return false
		'''
		return self.display_order == 0

	def delete(self, *args, **kwargs):
		'''
		Always keep display_order as consecutive integers to avoid errors
		'''
		super(ProductPhoto, self).delete(*args, **kwargs)

		for index, image in enumerate(self.product.images.all()):

			image.display_order = index
			image.save()

	def save(self, *args, **kwargs):
		'''

		'''
		images_count = self.number_of_images()

		if images_count == 0:
			self.display_order = 0

		else:
			self.display = images_count

		super(ProductPhoto, self).save(*args, **kwargs)

	def number_of_images(self):
		'''
		Aantal afbeeldingen die momenteel in stock zijn
		'''
		return len(self.product.images.all())


