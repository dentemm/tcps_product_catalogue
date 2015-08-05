# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0002_auto_20150715_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='name',
            field=models.CharField(unique=True, max_length=255, verbose_name='Name'),
        ),
    ]
