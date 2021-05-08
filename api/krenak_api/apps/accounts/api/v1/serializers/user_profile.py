from rest_framework import serializers

from krenak_api.apps.accounts.models import UserAccount
# from krenak_api.apps.mentorships.serializers import MentorshipSerializer

class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()
    role = serializers.SerializerMethodField('get_enrollment_type')

    class Meta:
        model = UserAccount
        fields = ("id", "email", "first_name", "last_name", "birthdate", "role")

    def get_enrollment_type(self, user):
        return user.enrollments.first().enrollment_type