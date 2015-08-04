# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Painter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=127, null=True, blank=True)),
                ('nationality', models.CharField(max_length=127, null=True, blank=True)),
                ('date_of_birth', models.CharField(max_length=127, null=True, blank=True)),
                ('date_of_death', models.CharField(max_length=127, null=True, blank=True)),
                ('history', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image1', models.ImageField(upload_to=b'paintings/', null=True, verbose_name=b'img', blank=True)),
                ('price', models.CharField(max_length=127, null=True, blank=True)),
                ('title', models.CharField(max_length=127, null=True, blank=True)),
                ('markings', models.CharField(max_length=127, null=True, blank=True)),
                ('original_currency', models.CharField(max_length=127, null=True, blank=True)),
                ('price_original_currency', models.IntegerField(null=True, blank=True)),
                ('price_dollars', models.IntegerField(null=True, blank=True)),
                ('currency', models.CharField(max_length=5, null=True, blank=True)),
                ('exhibited', models.TextField(null=True, blank=True)),
                ('edition', models.CharField(max_length=127, null=True, blank=True)),
                ('condition', models.CharField(max_length=127, null=True, blank=True)),
                ('year', models.IntegerField(null=True, blank=True)),
                ('estimate', models.CharField(max_length=127, null=True, blank=True)),
                ('low_estimate', models.IntegerField(null=True, blank=True)),
                ('high_estimate', models.IntegerField(null=True, blank=True)),
                ('measurements', models.CharField(max_length=256, null=True, blank=True)),
                ('url', models.URLField(max_length=511, null=True, blank=True)),
                ('sizenotes', models.CharField(max_length=127, null=True, blank=True)),
                ('provenance', models.TextField(null=True, blank=True)),
                ('auction_data', models.CharField(max_length=127, null=True, blank=True)),
                ('lot', models.CharField(max_length=127, null=True, blank=True)),
                ('description', models.CharField(max_length=256, null=True, blank=True)),
                ('literature', models.TextField(null=True, blank=True)),
                ('materials', models.CharField(max_length=127, null=True, blank=True)),
                ('sale_date', models.CharField(max_length=127, null=True, blank=True)),
                ('premium_hammer', models.CharField(max_length=127, null=True, blank=True)),
                ('width', models.FloatField(null=True, blank=True)),
                ('height', models.FloatField(null=True, blank=True)),
                ('depth', models.FloatField(null=True, blank=True)),
                ('nationality', models.CharField(max_length=127, null=True, blank=True)),
                ('RFC', models.CharField(max_length=127, null=True, blank=True)),
                ('painter', models.ForeignKey(to='blouin.Painter')),
            ],
        ),
    ]
