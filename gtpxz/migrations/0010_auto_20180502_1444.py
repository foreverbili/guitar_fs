# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 06:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtpxz', '0009_auto_20180502_1443'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gtp',
            name='gtp',
            field=models.FileField(blank=True, null=True, upload_to='static/gtpxz/gtps/%Y/%m/%d/'),
        ),
    ]
