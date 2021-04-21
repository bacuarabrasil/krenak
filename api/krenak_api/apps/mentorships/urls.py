from django.urls import path

from .views import MentorshipDetailsAPIView, MentorshipListCreateAPIView


urlpatterns = [
    path("mentorships/", MentorshipListCreateAPIView.as_view(), name="mentorship-list"),
    path("mentorships/<id>/", MentorshipDetailsAPIView.as_view(), name="mentorship-details"),
]
