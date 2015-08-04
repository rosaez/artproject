# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0011_auto_20150724_0644'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='materials_dummy2',
            field=models.CharField(max_length=127, null=True, blank=True),
        ),
    ]
