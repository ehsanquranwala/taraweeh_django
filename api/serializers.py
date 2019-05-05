from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'groups')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

class ProgramSerializer(serializers.ModelSerializer):
    program_type_name = serializers.CharField(source='program_type.name')
    place_name = serializers.CharField(source='place.name')
    address = serializers.CharField(source='place.address')
    area = serializers.CharField(source='place.area.name')
    city_town = serializers.CharField(source='place.city_town.name')
    region = serializers.CharField(source='place.city_town.region.name')
    country = serializers.CharField(source='place.city_town.region.country.name')
    speaker_name = serializers.CharField(source='speaker.name')
    organization_name = serializers.CharField(source='organization.name')
    class Meta:
        model = Program
        fields = ('start','end','timing','arrangements_for','phone1','phone2','program_type','program_type_name',
                  'place','place_name','address','area','city_town','region','country',
                  'speaker','speaker_name','organization','organization_name')