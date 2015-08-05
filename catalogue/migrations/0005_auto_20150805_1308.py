# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0004_auto_20150805_1252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productphoto',
            name='display_order',
            field=models.PositiveIntegerField(default=0, unique=True, verbose_name='Display order'),
        ),
    ]
