from __future__ import unicode_literals
from django.db import models


class Person(models.Model):
    id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50, verbose_name="First name", db_index=True)
    LastName = models.CharField(max_length=50, verbose_name="Last name", db_index=True)
    AddressId = models.IntegerField(blank=True, null=True, verbose_name="Address ID", db_index=True)


class Address(object):
    def __init__(self, *args, **kwargs):
        self.id = args[0].get("id", None)
        self.Street = args[0].get("Street", "")
        self.City = args[0].get("City", "")
        self.State = args[0].get("State", "")
        self.Country = args[0].get("Country", "")
        self.updated = args[0].get("updated", "")

    def __iter__(self):
        yield 'id', self.id
        yield 'Street', self.Street
        yield 'City', self.City
        yield 'State', self.State
        yield 'Country', self.Country
        yield 'updated', self.updated
