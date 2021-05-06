from django.urls import path

from .views import (
    EnrollmentDetailsAPIView,
    InterestDetailsAPIView,
    InterestListAPIView,
    EnrollmentListCreateAPIView
)


urlpatterns = [
    path("enrollments/", EnrollmentListCreateAPIView.as_view(), name="enrollment-listcreate"),
    path("enrollments/<id>/", EnrollmentDetailsAPIView.as_view(), name="enrollment-details"),
    path("interests/", InterestListAPIView.as_view(), name="interest-list"),
    path("interests/<id>/", InterestDetailsAPIView.as_view(), name="interest-details"),
]
