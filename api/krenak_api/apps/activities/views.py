from django.db.models import Q

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from .models import Activity, Task, Comment

from .serializers import ActivitySerializer, TaskSerializer, CommentSerializer


class ActivityListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of enrollments or create new
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()


class ActivityDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = ActivitySerializer
    queryset = Activity.objects.all()
    lookup_field = "id"

class TaskListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of enrollments or create new
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()


class TaskDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    lookup_field = "id"

class CommentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of enrollments or create new
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()


class CommentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    lookup_field = "id"
