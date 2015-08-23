# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20150822_1503'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='icon',
            field=models.ImageField(upload_to=b'category/icons', null=True, verbose_name='icoontje', blank=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(upload_to=b'category/images', null=True, verbose_name='afbeelding', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_folder',
            field=models.FileField(upload_to=b'product/documentation', null=True, verbose_name='Product folder', blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='user_manual',
            field=models.FileField(upload_to=b'product/documentation', null=True, verbose_name='User manual', blank=True),
        ),
        migrations.AlterField(
            model_name='productphoto',
            name='image',
            field=models.ImageField(upload_to=b'product/photos', max_length=255, verbose_name='foto'),
        ),
    ]
