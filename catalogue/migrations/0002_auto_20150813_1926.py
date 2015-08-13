# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subcategory',
            name='slug',
            field=models.CharField(max_length=255, verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='slug',
            field=models.CharField(max_length=255, verbose_name='Leverancier'),
        ),
    ]
