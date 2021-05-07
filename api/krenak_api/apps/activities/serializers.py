from rest_framework import serializers
from .models import Comment, Task, Activity


class CommentSerializer(serializers.ModelSerializer):
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
    class Meta:
        model = Activity
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def save(self, **kwargs):
        self.instance = super().save(**kwargs)
        return self.instance
