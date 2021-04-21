from rest_framework import serializers

from krenak_api.apps.enrollments.models import Enrollment
from krenak_api.apps.enrollments.serializers import EnrollmentSerializer
from krenak_api.apps.mentorships.models import Mentorship


class MentorshipSerializer(serializers.ModelSerializer):
    mentor_enrollment = EnrollmentSerializer(many=False)
    mentee_enrollment = EnrollmentSerializer(many=False)

    class Meta:
        model = Mentorship
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance
