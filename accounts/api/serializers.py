import datetime
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.utils import timezone
from rest_framework import serializers
from rest_framework.reverse import reverse as api_reverse
from rest_framework.serializers import (
    HyperlinkedIdentityField,
    ModelSerializer,
    SerializerMethodField
    )
from django.urls import reverse_lazy
from accounts.models import UserProfile
from subjects.api.serializers import SubjectSerializer
from locations.api.serializers import LocationSerializer
from analytics.models import ObjectViewed

User = get_user_model()

class TutorSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField()
    profile_image = serializers.SerializerMethodField()
    link = serializers.SerializerMethodField()
    work_experience = serializers.SerializerMethodField()
    city = LocationSerializer(read_only=True)
    tutor_subjects = SerializerMethodField()
    # subjects = SubjectSerializer(read_only=True, many=True)
    view_count = SerializerMethodField()

    class Meta:
        model = UserProfile
        fields = [
            'full_name',
            'profile_image',
            'link',
            'city',
            'work_experience',
            'tutor_subjects',
            'view_count',
        ]

    def get_full_name(self, obj):
        first_name = obj.first_name
        last_name = obj.last_name
        full_name = first_name + ' ' + last_name
        return full_name

    def get_profile_image(self, obj):
        return obj.get_image_url()

    def get_link(self, obj):
        return obj.get_absolute_url() + str(obj.id) + '/channel/'

    def get_work_experience(self, obj):
        experience = str(obj.work_experience) + ' years'
        return experience

    def get_view_count(self, obj):
        content_type = ContentType.objects.get_for_model(UserProfile)
        top_tutors = ObjectViewed.objects.filter(content_type=content_type)
        top_tutor = top_tutors.filter(object_id=obj.id)
        total = 0
        if top_tutor:
            for tutor in top_tutor:
                total += tutor.count
        return total

    def get_tutor_subjects(self, obj):
        subjects = obj.get_subjects()
        return subjects


