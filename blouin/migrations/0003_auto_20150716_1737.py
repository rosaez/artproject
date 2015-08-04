# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0002_auto_20150716_1727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='painter',
            field=models.CharField(max_length=127, null=True, blank=True),
        ),
        migrations.DeleteModel(
            name='Painter',
        ),
    ]
