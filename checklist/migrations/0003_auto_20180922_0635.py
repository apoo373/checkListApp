# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-22 06:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checklist', '0002_auto_20180922_0633'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklist',
            name='timeCreated',
            field=models.DateTimeField(auto_now_add=True, verbose_name='timeCreated'),
        ),
    ]