# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-02 08:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20180502_1644'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='type',
            field=models.CharField(blank=True, choices=[('second', '技术贴'), ('third', '公告贴'), ('first', '水一贴'), ('third', '交♂易贴')], max_length=50),
        ),
    ]