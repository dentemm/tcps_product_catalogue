# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0006_auto_20150823_0724'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(verbose_name='slug', blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug', blank=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='slug',
            field=models.SlugField(unique=True, verbose_name='slug', blank=True),
        ),
    ]
