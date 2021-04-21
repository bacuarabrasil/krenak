from django.urls import path

from .views import (
    EnrollmentCreateAPIView,
    EnrollmentDetailsAPIView,
    EnrollmentListAPIView,
    InterestDetailsAPIView,
    InterestListAPIView,
)


urlpatterns = [
    path("enrollments/", EnrollmentCreateAPIView.as_view(), name="enrollment-create"),
    path("enrollments/", EnrollmentListAPIView.as_view(), name="enrollment-list"),
    path("enrollments/<id>/", EnrollmentDetailsAPIView.as_view(), name="enrollment-details"),
    path("interests/", InterestListAPIView.as_view(), name="interest-list"),
    path("interests/<id>/", InterestDetailsAPIView.as_view(), name="interest-details"),
]
