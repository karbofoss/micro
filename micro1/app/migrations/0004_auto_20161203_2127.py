# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 19:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0003_auto_20161203_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]