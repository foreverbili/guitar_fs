# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-03 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20180502_1655'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.CharField(blank=True, choices=[('third', '交♂易贴'), ('first', '水一贴'), ('second', '技术贴'), ('third', '公告贴')], max_length=50),
        ),
    ]