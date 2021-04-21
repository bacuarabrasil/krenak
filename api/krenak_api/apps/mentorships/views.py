from django.db.models import Q

from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from krenak_api.apps.mentorships.models import Mentorship

from .serializers import MentorshipSerializer


class MentorshipListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of enrollments or create new
    """

    permission_classes = [IsAuthenticated]
    serializer_class = MentorshipSerializer

    def get_queryset(self, *args, **kwargs):
        queryset = Mentorship.objects.filter(
            Q(mentee_enrollment__enrollee__id=self.request.user.id)
            | Q(mentor_enrollment__enrollee_id=self.request.user.id)
        ).select_related("mentor_enrollment", "mentee_enrollment")
        return queryset


class MentorshipDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = MentorshipSerializer
    queryset = Mentorship.objects.all()
    lookup_field = "id"

    def get_queryset(self, *args, **kwargs):
        queryset = Mentorship.objects.filter(
            Q(mentee_enrollment__enrollee__id=self.request.user.id)
            | Q(mentor_enrollment__enrollee_id=self.request.user.id)
        ).select_related("mentor_enrollment", "mentee_enrollment")
        return queryset
