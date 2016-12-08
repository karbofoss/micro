from django.contrib import admin
from app.models import *


class PersonAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'LastName', 'AddressId')


admin.site.register(Person, PersonAdmin)
