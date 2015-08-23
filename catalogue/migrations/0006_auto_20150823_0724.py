# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0005_auto_20150823_0709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='logo',
            field=models.ImageField(upload_to=b'supplier/logo', max_length=255, verbose_name='logo', blank=True),
        ),
    ]
