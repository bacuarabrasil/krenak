from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated

from krenak_api.apps.enrollments.models import Enrollment, Interest

from .serializers import EnrollmentSerializer, InterestSerializer


class EnrollmentListCreateAPIView(ListCreateAPIView):
    """
    API view to retrieve list of enrollments or create new
    """

    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()


class EnrollmentDetailsAPIView(RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update or delete enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = EnrollmentSerializer
    queryset = Enrollment.objects.all()
    lookup_field = "id"


class InterestListAPIView(ListAPIView):
    """
    API view to retrieve list of enrollments
    """

    permission_classes = [IsAuthenticated]
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()


class InterestDetailsAPIView(RetrieveAPIView):
    """
    API view to retrieve interests
    """

    permission_classes = [IsAuthenticated]
    serializer_class = InterestSerializer
    queryset = Interest.objects.all()
    lookup_field = "id"
