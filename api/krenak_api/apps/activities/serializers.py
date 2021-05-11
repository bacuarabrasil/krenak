from rest_framework import serializers
from .models import Comment, Task, Activity
from krenak_api.apps.accounts.api.v1.serializers.user_profile import UserProfileSerializer

class CommentCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance

class CommentSerializer(serializers.ModelSerializer):
    author = UserProfileSerializer(many=False, read_only=True)
    class Meta:
        model = Comment
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance


class ActivitySerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Activity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance
