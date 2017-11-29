"""gardastations URL Configuration

Written with reference to the Django Rest Framework tutorials on www.django-rest-framework.org/
Most notably http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

"""
from django.conf.urls import url
from django.contrib.gis import admin
from rest_framework.urlpatterns import format_suffix_patterns
from stations.views import UserViewSet, StationViewSet, api_root

station_list = StationViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
station_detail = StationViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
user_list = UserViewSet.as_view({
    'get': 'list'
})
user_detail = UserViewSet.as_view({
    'get': 'retrieve'
})

urlpatterns = format_suffix_patterns([
    url(r'^$', api_root),
    url(r'^stations/$', station_list, name='station-list'),
    url(r'^stations/(?P<pk>[0-9]+)/$', station_detail, name='gardastations-detail'),
    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    url(r'^admin/', admin.site.urls),
])