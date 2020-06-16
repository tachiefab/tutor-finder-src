from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from locations.models import Location

class LocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = [
            'name',
        ]

    