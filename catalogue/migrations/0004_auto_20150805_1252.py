# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0003_auto_20150805_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_code',
            field=models.CharField(unique=True, max_length=128, blank=True),
        ),
        migrations.AlterField(
            model_name='subcategory',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='Name'),
        ),
    ]
