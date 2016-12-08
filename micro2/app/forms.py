from django import forms
from django.forms import HiddenInput
from .models import Address


class AddressForm(forms.ModelForm):
    # id = forms.HiddenInput()
    # FirstName = forms.CharField(label='First name', max_length=50)
    # LastName = forms.CharField(label='Last name', max_length=50)

    class Meta:
        model = Address
        fields = ('id', 'Street', 'City', 'State', 'Country')
        exclude = ('updated',)
        widgets = {
            'id': HiddenInput,
        }
