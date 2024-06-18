"""
Database models.
"""
from django.db import models

from django.conf import settings


class Group(models.Model):
    """Group to collect tasks."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    title = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.title


class Task(models.Model):
    """Task object."""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.CASCADE,
        null=True
    )
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    deadline = models.DateField()
    complexity = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title
