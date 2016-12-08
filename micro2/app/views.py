from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from .models import Address
from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import AddressSerializer
from .forms import AddressForm


def index(request):
    context = dict()
    context['addresses'] = Address.objects.all()
    return render(request, 'app/index.html', context)


def address_edit(request, id=None, template='app/address_edit.html'):
    if request.method == 'POST':
        if id is None:
            form = AddressForm(request.POST, Address())
            template = 'app/address_add.html'
        else:
            address = get_object_or_404(Address, id=id)
            form = AddressForm(request.POST, instance=address)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        if id:
            address = Address.objects.get(id=id)
            form = AddressForm(instance=address)
        else:
            form = AddressForm(instance=Address())
            template = 'app/address_add.html'

    return render(request, template, {'form': form, 'id': id})


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all().order_by('id')
    serializer_class = AddressSerializer

