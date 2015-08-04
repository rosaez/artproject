# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blouin', '0008_auto_20150724_0145'),
    ]

    operations = [
        migrations.RenameField(
            model_name='painting',
            old_name='city',
            new_name='city_sale',
        ),
    ]
