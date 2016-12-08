from django.conf.urls import url, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'address', views.AddressViewSet)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^address/new/$', views.address_edit, {}, name='address_add'),
    url(r'^address/edit/(?P<id>\d+)/$', views.address_edit, {}, name='address_edit'),
    url(r'^api/v1/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
