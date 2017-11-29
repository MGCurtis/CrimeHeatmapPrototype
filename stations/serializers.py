"""

Written with reference to the Django Rest Framework tutorials on www.django-rest-framework.org/
Most notably http://www.django-rest-framework.org/tutorial/5-relationships-and-hyperlinked-apis/

"""
from django.contrib.auth.models import User
from rest_framework import serializers
from stations.models import GardaStations

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')

class StationSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = GardaStations
        fields = ('url', 'id', 'fid', 'name', 'blank', 'Sun', 'Address',
                  'Longitude', 'Latitude', 'County', 'Phone', 'StationID',
                  'Station', 'Mon_Fri', 'Sat')