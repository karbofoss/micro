from .models import Address
from rest_framework import serializers


class AddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Address
        fields = ('id', 'Street', 'City', 'State', 'Country', 'updated')
