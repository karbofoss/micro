from django import forms
from django.forms import HiddenInput, Select

from .models import Person


class PersonForm(forms.ModelForm):
    # id = forms.HiddenInput()
    # FirstName = forms.CharField(label='First name', max_length=50)
    # LastName = forms.CharField(label='Last name', max_length=50)

    class Meta:
        model = Person
        fields = ('id', 'FirstName', 'LastName', 'AddressId',)
        widgets = {
            'id': HiddenInput,
            'AddressId': Select(choices=(('1', '1111'), ('2', '22222')))
        }


class AddressForm(forms.Form):
    id = forms.HiddenInput()
    Street = forms.CharField(max_length=50, min_length=1, strip=True, label='Street')
    City = forms.CharField(max_length=50, min_length=1, strip=True, label='City')
    State = forms.CharField(max_length=50, min_length=1, strip=True, label='State')
    Country = forms.CharField(max_length=50, min_length=1, strip=True, label='Country')
