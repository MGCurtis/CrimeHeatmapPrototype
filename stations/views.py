"""

Written with reference to the Django Rest Framework tutorials on www.django-rest-framework.org/
Most notably http://www.django-rest-framework.org/tutorial/6-viewsets-and-routers/

"""

from django.contrib.auth.models import User
from rest_framework import viewsets, permissions
from stations.serializers import  UserSerializer, StationSerializer
from stations.models import GardaStations
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse



# Create your views here.


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class StationViewSet(viewsets.ModelViewSet):
    queryset = GardaStations.objects.all()
    serializer_class = StationSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly)

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'stations': reverse('station-list', request=request, format=format)
    })