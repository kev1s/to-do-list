# -*- coding: utf-8 -*-
# Generated by Django 1.9.11 on 2016-11-03 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='list',
            field=models.TextField(default=''),
        ),
    ]
