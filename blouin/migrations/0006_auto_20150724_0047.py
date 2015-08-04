# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0005_auto_20150724_0031'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='materials_dummy',
            field=models.CharField(max_length=127, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='painting',
            name='sale_year',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
