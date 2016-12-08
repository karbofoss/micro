from __future__ import unicode_literals

from django.db import models


class Address(models.Model):
    Street = models.CharField(max_length=50, verbose_name="Street", db_index=True)
    City = models.CharField(max_length=50, verbose_name="City", db_index=True)
    State = models.CharField(max_length=50, verbose_name="State", db_index=True)
    Country = models.CharField(max_length=50, verbose_name="Country", db_index=True)
    updated = models.DateTimeField(blank=True, null=True, auto_now=True, db_index=True)
