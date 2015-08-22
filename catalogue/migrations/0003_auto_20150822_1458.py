# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20150822_1442'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='description',
        ),
        migrations.RemoveField(
            model_name='subcategory',
            name='description',
        ),
        migrations.RemoveField(
            model_name='supplier',
            name='description',
        ),
        migrations.AddField(
            model_name='subcategory',
            name='image',
            field=models.ImageField(upload_to=b'subcategory/images', null=True, verbose_name='afbeelding', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'category/icons/', null=True, verbose_name='icoontje', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=255, verbose_name='naam'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(unique=True, max_length=128, verbose_name='product code', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_folder',
            field=models.FileField(upload_to=b'product/documentation/', null=True, verbose_name='Product folder', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.CharField(max_length=255, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='product',
            name='user_manual',
            field=models.FileField(upload_to=b'product/documentation/', null=True, verbose_name='User manual', blank=True),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='alt_text',
            field=models.CharField(max_length=255, null=True, verbose_name='korte beschrijving', blank=True),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='datum toegevoegd'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='display_order',
            field=models.PositiveIntegerField(default=0, unique=True, verbose_name='weergave volgorde'),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='image',
            field=models.ImageField(upload_to=b'test/', max_length=255, verbose_name='foto'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='naam'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='parent_category',
            field=models.ForeignKey(related_name='subcategories', verbose_name=b'hoofdcategorie', to='catalogue.Category'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(unique=True, max_length=255, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='suppliers',
            field=models.ManyToManyField(related_name='categories', verbose_name='leverancier', to='catalogue.Supplier'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='logo',
            field=models.ImageField(upload_to=b'', max_length=255, verbose_name='logo', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='naam'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='slug',
            field=models.CharField(unique=True, max_length=255, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='website',
            field=models.URLField(verbose_name='website url', blank=True),
        ),
    ]
