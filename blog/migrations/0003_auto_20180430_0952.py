# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-30 01:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20180428_1328'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comblog',
        ),
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.CharField(blank=True, choices=[('third', '交♂易贴'), ('second', '技术贴'), ('third', '公告贴'), ('first', '水一贴')], max_length=50),
        ),
    ]
