from django.urls import path

from .views import EnrollmentDetailsAPIView, EnrollmentListCreateAPIView, InterestDetailsAPIView, InterestListAPIView


urlpatterns = [
    path("enrollments", EnrollmentListCreateAPIView.as_view(), name="enrollment-list"),
    path("enrollments/<id>/", EnrollmentDetailsAPIView.as_view(), name="enrollment-details"),
    path("interests", InterestListAPIView.as_view(), name="interest-list"),
    path("interests/<id>/", InterestDetailsAPIView.as_view(), name="interest-details"),
]
