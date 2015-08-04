# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='painter',
            field=models.ForeignKey(to='blouin.Painter', null=True),
        ),
    ]
