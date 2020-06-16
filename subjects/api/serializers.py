from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from subjects.models import Subject

class SubjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = [
            'name',
            'count',
            'active',
        ]

    