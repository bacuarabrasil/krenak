from rest_framework import serializers

from krenak_api.apps.accounts.api.v1.serializers.user_profile import UserProfileSerializer
from krenak_api.apps.enrollments.models import Enrollment, Interest


class InterestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interest
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance


class EnrollmentSerializer(serializers.ModelSerializer):
    interests = InterestSerializer(many=True, read_only=True)
    enrollee = UserProfileSerializer(many=False, read_only=True)

    class Meta:
        model = Enrollment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance


class EnrollmentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance
