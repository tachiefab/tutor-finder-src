from rest_framework import generics, permissions, pagination
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from .serializers import TutorSerializer
from accounts.models import UserProfile
from analytics.models import ObjectViewed

User = get_user_model()


class TopRatedTutorListAPIView(generics.ListAPIView):
	serializer_class = TutorSerializer

	def get_queryset(self, *args, **kwargs):
	    tutors = UserProfile.objects.filter(is_tutor=True)
	    return tutors


