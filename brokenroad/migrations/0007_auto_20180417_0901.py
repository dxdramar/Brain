# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-04-17 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brokenroad', '0006_brokenroad_deskripsi'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brokenroad',
            name='deskripsi',
            field=models.TextField(default='Isikan Deskripsi Kerusakan...', max_length=500),
        ),
    ]
