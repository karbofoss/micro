from django import template
from app.models import Address

register = template.Library()


@register.filter('hash')
def hash(dict_data, key):
    """
    usage example {{ your_dict|hash:your_key }}
    """
    if key:
        return dict_data.get(key)


@register.filter('address')
def address(dict_data, key):
    """
    usage example {{ your_dict|address:your_key }}
    """
    if key:
        a = dict_data.get(key)
        if isinstance(a, dict):
            return "%s, %s, %s, %s, %s" % (a['Street'], a['City'], a['State'], a['Country'], a['updated'])
        elif isinstance(a, Address):
            return "%s, %s, %s, %s, %s" % (a.Street, a.City, a.State, a.Country, a.updated)
