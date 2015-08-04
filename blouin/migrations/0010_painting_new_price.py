# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0009_auto_20150724_0311'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='new_price',
            field=models.FloatField(null=True, blank=True),
        ),
    ]
