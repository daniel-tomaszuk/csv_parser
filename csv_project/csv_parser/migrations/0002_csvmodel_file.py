# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-05 07:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('csv_parser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvmodel',
            name='file',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='csv_parser.CSVFile'),
        ),
    ]
