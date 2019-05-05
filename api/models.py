from django.db import models

class Speaker(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

class PlaceType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

class Region(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    country = models.ForeignKey('Country', models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class CityTown(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    region = models.ForeignKey('Region', models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class Area(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    city_town = models.ForeignKey('CityTown', models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class Place(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    address = models.CharField(max_length=255, null=False, blank=False)
    place_type = models.ForeignKey('PlaceType', models.SET_NULL, blank=True, null=True)
    city_town = models.ForeignKey('CityTown', models.SET_NULL, blank=True, null=True)
    area = models.ForeignKey('Area', models.SET_NULL, blank=True, null=True)
    def __str__(self):
        return self.name

class Organization(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

class ProgramType(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.name

class Program(models.Model):
    program_type = models.ForeignKey('ProgramType', models.SET_NULL, blank=True, null=True)
    place = models.ForeignKey('Place', models.SET_NULL, blank=True, null=True)
    speaker = models.ForeignKey('Speaker', models.SET_NULL, blank=True, null=True)
    organization = models.ForeignKey('Organization', models.SET_NULL, blank=True, null=True)
    start = models.CharField(max_length=255, null=False, blank=False)
    end = models.CharField(max_length=255, null=False, blank=False)
    timing = models.CharField(max_length=255, null=False, blank=False)
    arrangements_for = models.CharField(max_length=255, null=False, blank=False)
    phone1 = models.CharField(max_length=255, null=False, blank=False)
    phone2 = models.CharField(max_length=255, null=False, blank=False)
    def __str__(self):
        return self.program_type.name + ' @ ' + self.place.name + ' by ' + self.speaker.name