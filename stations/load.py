import os
from django.contrib.gis.utils import LayerMapping
from .models import GardaStations

station_mapping = {
    'fid' : 'fid',
    'name' : 'Name',
    'blank' : '_',
    'Sun' : 'Sun',
    'Address' : 'Address',
    'Longitude' : 'Longitude',
    'County' : 'County',
    'Phone' : 'Phone',
    'StationID' : 'Station',
    'Mon_Fri' : 'Mon_Fri',
    'Latitude' : 'Latitude',
    'Sat' : 'Sat',
    'point' : 'POINT',
}

stations_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'Garda_Stations3.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        GardaStations, stations_shp, station_mapping,
        transform=False, encoding='iso-8859-1',
    )
    lm.save(strict=True, verbose=verbose)