"""
Views for the task APIs
"""
from rest_framework import (
    viewsets,
    mixins,
)

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from todo.models import (
    Task,
    Group,
)
from todo import serializers


class TaskViewSet(viewsets.ModelViewSet):
    """View for manage task APIs."""
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve tasks for authenticated user."""
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user
            ).order_by('-id').distinct()

    def perform_create(self, serializer):
        """Create a new task."""
        serializer.save(user=self.request.user)


class GroupViewSet(viewsets.ModelViewSet):
    """Manage groups in the database."""
    serializer_class = serializers.GroupSerializer
    queryset = Group.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve groups for authenticated user."""
        queryset = self.queryset
        return queryset.filter(
            user=self.request.user
            ).order_by('-id').distinct()

    def perform_create(self, serializer):
        """Create a new group for task."""
        serializer.save(user=self.request.user)
