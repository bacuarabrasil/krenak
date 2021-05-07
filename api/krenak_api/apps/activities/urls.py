from django.urls import path

from .views import (
    ActivityListCreateAPIView,
    ActivityDetailsAPIView,
    CommentListCreateAPIView,
    CommentDetailsAPIView,
    TaskListCreateAPIView,
    TaskDetailsAPIView,
)


urlpatterns = [
    path("activities/", ActivityListCreateAPIView.as_view(), name="activitie-listcreate"),
    path("activities/<id>/", ActivityDetailsAPIView.as_view(), name="activitie-details"),
    path("comments/", CommentListCreateAPIView.as_view(), name="activitie-listcreate"),
    path("comments/<id>/", CommentDetailsAPIView.as_view(), name="activitie-details"),
    path("tasks/", TaskListCreateAPIView.as_view(), name="activitie-listcreate"),
    path("tasks/<id>/", TaskDetailsAPIView.as_view(), name="activitie-details"),
]
