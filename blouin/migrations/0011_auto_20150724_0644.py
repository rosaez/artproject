# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0010_painting_new_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='description',
            field=models.TextField(null=True, blank=True),
        ),
    ]
