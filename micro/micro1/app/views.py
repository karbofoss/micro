# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import json

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404

from micro1 import settings
from . import models
from . import forms
import coreapi
import requests


def save_address(address=models.Address):
    resp = None
    if address.id:
        resp = requests.put(settings.API_URL + 'address/' + address.id + '/', auth=('admin', 'Qwerty123'),
                            json=address.__dict__)
        if resp.status_code != 200:
            # This means something went wrong.
            raise Exception('POST /address/{} {} {}'.format(address.id, resp.status_code, resp.content))
    else:
        resp = requests.post(settings.API_URL + 'address/', auth=('admin', 'Qwerty123'), json=address.__dict__)
        if resp.status_code != 201:
            # This means something went wrong.
            raise Exception('POST /address/ {} {}'.format(resp.status_code, resp.content))
    print('Created address. ID: {}'.format(resp.json()["id"]))


def get_address(id=None):
    if id:
        resp = requests.get(settings.API_URL + 'address/' + id, auth=('admin', 'Qwerty123'))
        if resp.status_code != 200:
            raise Exception('GET /address/{} {} {}'.format(id, resp.status_code, resp.content))
        address = resp.json()
        return models.Address(address)
    return None


def get_addresses():
    addresses = dict()
    resp = requests.get(settings.API_URL + 'address/', auth=('admin', 'Qwerty123'))
    if resp.status_code != 200:
        # This means something went wrong.
        raise Exception('GET /address/ {} {}'.format(resp.status_code, resp.content))
    for a in resp.json()['results']:
        addresses[a['id']] = models.Address(dict(a))
    return addresses


# def get_addresses2():
#     # test_post_requests()
#     # test_requests()
#     addresses = dict()
#     credentials = {settings.API_HOST: 'Basic ' + coreapi.compat.b64encode('admin:Qwerty123')}
#     transport = coreapi.transports.HTTPTransport(credentials=credentials)
#     client = coreapi.Client(transports=(transport,))
#     schema2 = client.get(settings.API_URL)
#     schema = client.get(settings.API_URL + 'address/')
#     for a in schema['results']:
#         addresses[a['id']] = dict(a)
#     #        print(addresses[a['id']])
#     return addresses


def index(request):
    context = dict()
    addresses = get_addresses()
    context['persons'] = models.Person.objects.all()
    context['addresses'] = addresses
    return render(request, 'app/index.html', context)


def person_edit(request, id=None, template='app/person_edit.html'):
    if request.method == 'POST':
        if id is None:
            form = forms.PersonForm(request.POST, models.Person())
            template = 'app/person_add.html'
        else:
            person = get_object_or_404(models.Person, id=id)
            form = forms.PersonForm(request.POST, instance=person)
            # form = forms.PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            form.save()
            # person, cr = models.Person.objects.update_or_create(defaults=form.cleaned_data)
            return HttpResponseRedirect('/')

            # if a GET (or any other method) we'll create a blank form
    else:
        if id:
            person = models.Person.objects.get(id=id)
            form = forms.PersonForm(instance=person)
        else:
            form = forms.PersonForm(instance=models.Person())
            template = 'app/person_add.html'
    addresses = get_addresses()
    choices = list()
    choices.append((None, 'Not selected'))
    for k in addresses:
        v = addresses[k]
        address = '%s, %s, %s, %s' % (v.Street, v.City, v.State, v.Country)
        choices.append((k, address))
    form.fields['AddressId'].widget.choices = choices
    return render(request, template, {'form': form, 'id': id})


def address_edit(request, id=None, template='app/address_edit.html'):
    if request.method == 'POST':
        if id is None:
            form = forms.AddressForm(request.POST)
            template = 'app/address_add.html'
        else:
            address = get_address(id=id)
            form = forms.AddressForm(request.POST, address)
            # form = forms.PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # form.save()
            form.cleaned_data['id'] = id
            address = models.Address(form.cleaned_data)

            save_address(address)
            # person, cr = models.Person.objects.update_or_create(defaults=form.cleaned_data)
            return HttpResponseRedirect('/')

            # if a GET (or any other method) we'll create a blank form
    else:
        if id:
            address = get_address(id)
            form = forms.AddressForm(dict(address))
        else:
            form = forms.AddressForm()
            template = 'app/address_add.html'

    return render(request, template, {'form': form, 'id': id})
