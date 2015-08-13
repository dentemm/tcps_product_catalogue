# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import catalogue.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Naam')),
                ('image', models.ImageField(max_length=255, upload_to=b'categories', null=True, verbose_name='Afbeelding', blank=True)),
                ('slug', models.SlugField(unique=True, max_length=255, verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'categorie',
                'verbose_name_plural': 'categorieen',
            },
            bases=(catalogue.models.MetaOptionsMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('product_code', models.CharField(unique=True, max_length=128, blank=True)),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('product_folder', models.FileField(upload_to=b'documentation', null=True, verbose_name='Product folder', blank=True)),
                ('user_manual', models.FileField(upload_to=b'documentation', null=True, verbose_name='User manual', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductPhoto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(max_length=255, upload_to=b'test')),
                ('alt_text', models.CharField(max_length=255, null=True, blank=True)),
                ('display_order', models.PositiveIntegerField(default=0, unique=True, verbose_name='Display order')),
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
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Naam')),
                ('slug', models.CharField(default=models.CharField(unique=True, max_length=255, verbose_name='Naam'), max_length=255, verbose_name='Slug')),
                ('description', models.TextField(null=True, verbose_name='Beschrijving', blank=True)),
                ('parent_category', models.ForeignKey(related_name='subcategories', verbose_name=b'Parent Category', to='catalogue.Category')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'subcategorie',
                'verbose_name_plural': 'subcategorieen',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255, verbose_name='Naam')),
                ('slug', models.CharField(default=models.CharField(unique=True, max_length=255, verbose_name='Naam'), unique=True, max_length=255, verbose_name='Leverancier')),
                ('description', models.TextField(null=True, verbose_name='Description', blank=True)),
                ('website', models.URLField(blank=True)),
                ('logo', models.ImageField(max_length=255, upload_to=b'', blank=True)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'leverancier',
                'verbose_name_plural': 'leveranciers',
            },
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
