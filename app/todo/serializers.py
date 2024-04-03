"""
Serializers for the recipe APIs
"""
from rest_framework import serializers

from todo.models import (
    Task,
)


class TaskSerializer(serializers.ModelSerializer):
    """Serializer for tasks."""
    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'deadline', 'complexity',
        ]
        read_only_fields = ['id']

    def create(self, validated_data):
        """Create a task."""
        task = Task.objects.create(**validated_data)
        return task

    def update(self, instance, validated_data):
        """Update task."""
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance


class TaskDetailSerializer(TaskSerializer):
    """Serializer for recipe detail view."""
    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + ['description', 'complexity']
