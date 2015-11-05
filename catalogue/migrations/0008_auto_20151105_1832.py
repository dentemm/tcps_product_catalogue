# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0007_auto_20150823_0737'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_folder',
            field=models.FileField(upload_to=b'product/documentation', null=True, verbose_name='product folder', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='user_manual',
            field=models.FileField(upload_to=b'product/documentation', null=True, verbose_name='manual', blank=True),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='product',
            field=models.ForeignKey(related_name='images', verbose_name='product', to='catalogue.Product'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(related_name='subcategories', verbose_name='categorie', to='catalogue.Category'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='website',
            field=models.URLField(verbose_name='link naar website', blank=True),
        ),
    ]
