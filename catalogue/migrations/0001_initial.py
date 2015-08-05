# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('image', models.ImageField(max_length=255, upload_to=b'categories', null=True, verbose_name='Image', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(max_length=128, blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('product_folder', models.FileField(upload_to=b'documentation', null=True, verbose_name='Product folder', blank=True)),
                ('user_manual', models.FileField(upload_to=b'documentation', null=True, verbose_name='User manual', blank=True)),
                ('technical_manual', models.FileField(upload_to=b'documentation', null=True, verbose_name='Technical manual', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(max_length=255, upload_to=b'test')),
                ('display_order', models.PositiveIntegerField(default=0, verbose_name='Display order')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('product', models.ForeignKey(related_name='images', verbose_name='Product', to='catalogue.Product')),
            ],
            options={
                'verbose_name': 'Product image',
                'verbose_name_plural': 'Product images',
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('parent_category', models.ForeignKey(related_name='subcategories', verbose_name=b'Parent Category', to='catalogue.Category')),
            ],
            options={
                'verbose_name': 'Subcategory',
                'verbose_name_plural': 'Subcategories',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('website', models.URLField(blank=True)),
                ('logo', models.ImageField(max_length=255, upload_to=b'', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='subcategory',
            name='suppliers',
            field=models.ManyToManyField(related_name='categories', to='catalogue.Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='subcategory',
            field=models.ForeignKey(related_name='products', verbose_name='Subcategory', to='catalogue.SubCategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='supplier',
            field=models.ForeignKey(related_name='products', verbose_name='Supplier', to='catalogue.Supplier'),
        ),
    ]
