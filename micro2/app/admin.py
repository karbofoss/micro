from django.contrib import admin
from app.models import *


class AddressAdmin(admin.ModelAdmin):
    list_display = ('id', 'Street', 'City', 'State', 'Country', 'updated')


admin.site.register(Address, AddressAdmin)
