# from django.contrib import admin
from django.urls import path
from .views import (
				TutorChannelView, 
				TutorUpdateView, 
				TutorDetailView, 
				TutorListView,
				UserSignUpView
				)

urlpatterns = [
    path('tutor/', TutorDetailView.as_view(), name='profile'),
    path('tutor/<int:pk>/channel/', TutorChannelView.as_view(), name='channel'),
    path('tutor/<int:pk>/update/', TutorUpdateView.as_view(), name='update'),
    path('tutor-list/', TutorListView.as_view(), name='tutor-list'),
    path('signup/', UserSignUpView.as_view(), name='signup'),
]
