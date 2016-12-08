from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^person/new/$', views.person_edit, {}, name='person_add'),
    url(r'^person/edit/(?P<id>\d+)/$', views.person_edit, {}, name='person_edit'),
    url(r'^address/new/$', views.address_edit, {}, name='address_add'),
    url(r'^address/edit/(?P<id>\d+)/$', views.address_edit, {}, name='address_edit'),
]
