from django.urls import path
from .views import (
            TopRatedTutorListAPIView,
            )

urlpatterns = [
    # url(r'^top-rated-tutor/$', TopRatedTutorListAPIView.as_view(), name='list'),
    path('top-rated-tutor/', TopRatedTutorListAPIView.as_view(), name='top-rated-tutor'),
    ]
