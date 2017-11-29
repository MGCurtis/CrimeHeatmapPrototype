from django.contrib.gis.db import models

# Create your models here.

class GardaStations(models.Model):
    fid = models.CharField(max_length=80)
    name = models.CharField(max_length=80);
    blank = models.CharField(max_length=80);
    Sun = models.CharField(max_length=80);
    Address = models.CharField(max_length=80);
    Longitude = models.CharField(max_length=80);
    Latitude = models.CharField(max_length=80);
    County = models.CharField(max_length=80);
    Phone = models.CharField(max_length=80);
    StationID = models.CharField(max_length=80);
    Station = models.CharField(max_length=80);
    Mon_Fri = models.CharField(max_length=80);
    Sat = models.CharField(max_length=80);

    point = models.PointField();

    def __str__(self):
        return self.name