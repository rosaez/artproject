# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0004_painting_markings_dummy'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='auction_house',
            field=models.CharField(max_length=127, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='painting',
            name='provenance_dummy',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
