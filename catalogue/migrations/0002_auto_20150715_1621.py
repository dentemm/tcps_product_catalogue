# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalogue', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='technical_manual',
        ),
        migrations.AddField(
            model_name='productphoto',
            name='alt_text',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
