# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gtpxz', '0005_auto_20180430_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(blank=True, choices=[('man', '男'), ('woman', '女')], max_length=50),
        ),
    ]