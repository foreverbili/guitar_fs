# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 06:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20180502_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.CharField(blank=True, choices=[('third', '公告贴'), ('first', '水一贴'), ('third', '交♂易贴'), ('second', '技术贴')], max_length=50),
        ),
    ]