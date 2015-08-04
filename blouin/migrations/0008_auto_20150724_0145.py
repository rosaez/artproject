# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0007_painting_dead_soon'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='certificate_dummy',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='painting',
            name='city',
            field=models.CharField(max_length=127, null=True, blank=True),
        ),
    ]
