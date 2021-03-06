# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-28 01:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('published_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True)),
                ('type', models.CharField(blank=True, choices=[('third', '公告贴'), ('third', '交♂易贴'), ('second', '技术贴'), ('first', '水一贴')], max_length=50)),
            ],
        ),
    ]
