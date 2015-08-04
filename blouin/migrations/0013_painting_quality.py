# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0012_painting_materials_dummy2'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='quality',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
