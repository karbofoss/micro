# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-03 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='AddressId',
            field=models.IntegerField(blank=True, null=True, verbose_name='Address ID'),
        ),
        migrations.AlterField(
            model_name='person',
            name='FirstName',
            field=models.CharField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='person',
            name='LastName',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
    ]
