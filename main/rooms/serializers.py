from rest_framework import serializers
from rooms import models
from django.contrib.auth.models import User
from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers as xxx
from drf_extra_fields.fields import Base64ImageField

import json


class RoomSerializer(serializers.ModelSerializer):
    
    owner_first_name = serializers.ReadOnlyField(source='owner.first_name')
    owner_last_name = serializers.ReadOnlyField(source='owner.last_name')
    pictures = serializers.SerializerMethodField()
    services_description = serializers.SerializerMethodField()
    
    def get_pictures(self, data):
        # fare meglio
        # https://stackoverflow.com/questions/44313073/django-rest-serializers-based-on-multiple-querysets
        queryset = models.RoomImage.objects.filter(room=data.id).values('id','file')
        #return xxx.serialize('json', queryset, fields=('file'))
        return json.loads(json.dumps(list(queryset), cls=DjangoJSONEncoder))
    
    def get_services_description(self, data):
        # fare meglio
        # https://stackoverflow.com/questions/44313073/django-rest-serializers-based-on-multiple-querysets
        queryset = models.RoomService.objects.filter(room=data.id).values('id','category','title')
        #return xxx.serialize('json', queryset, fields=('file'))
        return json.loads(json.dumps(list(queryset), cls=DjangoJSONEncoder))

    class Meta:

        fields = (
            'id',
            'published',
            'owner',
            'owner_first_name',
            'owner_last_name',
            'title',
            'description',
            'price',
            'creation_date',
            'services',
            'services_description',
            'pictures',
            'category',
            'guests',
            'bedrooms',
            'beds',
            'bathrooms',
            'bathrooms_isprivate',
            'position_full_address',
            'position_country',
            'position_city',
            'position_locality_regione',
            'position_locality_provincia',
            'position_locality_comune',
            'position_street',
            'position_street_number',
            'position_zipcode',
            'position_geometry_lat',
            'position_geometry_lng',
            'creation_progress',
        )
        model = models.Room


class RoomImageSerializer(serializers.ModelSerializer):
    file=Base64ImageField()
    class Meta:
        model = models.RoomImage
        fields = '__all__'

class RoomServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RoomService
        fields = '__all__'