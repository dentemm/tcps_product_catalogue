from django.db import models
from django.utils.translation import ugettext as _
from django.conf import settings
from django.template.defaultfilters import slugify

#from autoslug import AutoSlugField

# Create your models here.


class Category(models.Model):

	name = models.CharField(_('Name'), max_length=255, unique=True)
	# description = models.TextField(_('Description'), null=True, blank=True) //Provided by django cms
	image = models.ImageField(_('Image'), upload_to='categories', blank=True, null=True, max_length=255)
	slug = models.SlugField(_('Slug'), unique=True, max_length=255)


	class Meta:
		app_label = 'catalogue'
		ordering = ['name']
		verbose_name = _('category')
		verbose_name_plural = _('categories')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return '/dashboard/' 

class SubCategory(models.Model):

	name = models.CharField(_('Name'), max_length=255, unique=True)
	description = models.TextField(_('Description'), null=True, blank=True)
	parent_category = models.ForeignKey(Category, verbose_name='Parent Category', related_name='subcategories')
	suppliers = models.ManyToManyField('Supplier', related_name='categories')

	subcategories = models.Manager

	class Meta:
		app_label = 'catalogue'
		verbose_name = _('Subcategory')
		verbose_name_plural = _('Subcategories')

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name


class Supplier(models.Model):

	name = models.CharField(_('Name'), max_length=255, unique=True)
	description = models.TextField(_('Description'), null=True, blank=True)
	website = models.URLField(blank=True)
	logo = models.ImageField(max_length=255, blank=True)

	suppliers = models.Manager()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name



class Product(models.Model):

	product_code = models.CharField(max_length=128, blank=True, unique=True)
	name = models.CharField(max_length=255, verbose_name=_('Name'))
	description = models.TextField(null=True, blank=True, verbose_name=_('Description'))
	supplier = models.ForeignKey(Supplier, verbose_name=_('Supplier'), related_name='products')
	subcategory = models.ForeignKey(SubCategory, verbose_name=_('Subcategory'), related_name='products')

	product_folder = models.FileField(_('Product folder'), upload_to='documentation', null=True, blank=True)
	user_manual = models.FileField(_('User manual'), upload_to='documentation', null=True, blank=True)
	#technical_manual = models.FileField(_('Technical manual'), upload_to='documentation', null=True, blank=True) //rejected by tcps

	products = models.Manager()

	def __unicode__(self):
		return self.name

	def __str__(self):
		return self.name

class ProductPhoto(models.Model):

	product = models.ForeignKey(Product, verbose_name=_('Product'), related_name='images')
	image = models.ImageField(upload_to='test', max_length=255)
	alt_text = models.CharField(max_length=255, null=True, blank=True)

	display_order = models.PositiveIntegerField(_('Display order'), default=0, unique=True)
	date_created = models.DateTimeField(_('Date created'), auto_now_add=True)

	class Meta:

		app_label = 'catalogue'
		verbose_name = _('Product image')
		verbose_name_plural = _('Product images')

	def __string__(self):

		return "Image %s of %s" % (self.display_order + 1, self.product)

	def __unicode__(self):
		return "Image %s of %s" % (self.display_order + 1, self.product)

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


