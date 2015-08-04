# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0006_auto_20150724_0047'),
    ]

    operations = [
        migrations.AddField(
            model_name='painting',
            name='dead_soon',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
