# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0003_auto_20150716_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='markings_dummy',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
