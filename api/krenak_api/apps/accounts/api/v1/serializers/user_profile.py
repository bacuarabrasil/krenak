from rest_framework import serializers

from krenak_api.apps.accounts.models import UserAccount


class UserProfileSerializer(serializers.ModelSerializer):
    email = serializers.ReadOnlyField()

    class Meta:
        model = UserAccount
        fields = ("email", "first_name", "last_name", "birthdate")
