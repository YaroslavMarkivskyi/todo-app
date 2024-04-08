"""
Serializers for the recipe APIs
"""
from rest_framework import serializers

from todo.models import (
    Task,
    Group,
)


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for groups."""

    class Meta:
        model = Group
        fields = ['id', 'title']
        read_only_fields = ['id']


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for tasks."""
    group = GroupSerializer(many=True, required=False)

    class Meta:
        model = Task
        fields = [
            'id', 'group', 'title', 'description', 'deadline', 'complexity',
        ]
        read_only_fields = ['id']


# class TaskDetailSerializer(TaskSerializer):
#     """Serializer for recipe detail view."""
#     class Meta(TaskSerializer.Meta):
#         fields = TaskSerializer.Meta.fields + ['description', 'complexity']
