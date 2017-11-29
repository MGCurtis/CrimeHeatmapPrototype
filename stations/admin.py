from django.contrib.gis import admin
from .models import GardaStations

# Register your models here.

admin.site.register(GardaStations, admin.GeoModelAdmin)
