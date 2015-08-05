import itertools

from django import forms
from django.utils.text import slugify

from .models import Category

class AddCategoryForm(forms.ModelForm):

	class Meta:

		model = Category
		fields = (
			'name',
			'image',
		)

	def save(self):

		instance = super(AddCategoryForm, self).save(commit=False)
		instance.slug = orig = slugify(instance.name)

		# Add number to slug name in case of duplicate slug names (eg. some-categorie-2)
		for x in itertools.count(1):
			if not Category.objects.filter(slug=instance.slug).exists():
				break

			# Ensure slug length does not exceed max allowed 
			instance.slug = '%s-%d' % (orig[:max_length - len(str(x)) - 1], x)

		instance.save()

		return instance