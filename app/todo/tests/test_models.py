"""
Tests for models.
"""
from django.test import TestCase
from django.db.utils import IntegrityError
from django.contrib.auth import get_user_model

from datetime import date

from todo import models


class ModelTests(TestCase):
    """
    Test cases for  models.
    """
    def test_create_group(self):
        """Test creating a group to collect tasks."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        group = models.Group.objects.create(
            user=user,
            title="Group of tasks."
        )
        self.assertEqual(str(group), group.title)
        self.assertTrue(models.Group.objects.filter(pk=group.pk).exists())

    def test_create_group_without_user(self):
        """Test creating group without user raises error."""
        with self.assertRaises(IntegrityError):
            models.Group.objects.create(
                title="Group of tasks."
                )

    def test_create_task_without_group(self):
        """Test creating a task without group is succesfull."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        for complexity in (True, False):
            task = models.Task.objects.create(
                user=user,
                title='Some task title',
                description='Some task description',
                deadline=date(2024, 4, 2),
                complexity=complexity,
            )
            self.assertEqual(str(task), task.title)
            self.assertTrue(models.Task.objects.filter(pk=task.pk).exists())

    def test_create_task__with_group(self):
        """Test creating a task with group is succesfull."""
        user = get_user_model().objects.create_user(
            'test@example.com',
            'testpass123'
        )
        for complexity in (True, False):
            task = models.Task.objects.create(
                user=user,
                group=None,
                title='Some task title',
                description='Some task description',
                deadline=date(2024, 4, 2),
                complexity=complexity,
            )
            self.assertEqual(str(task), task.title)
            self.assertTrue(models.Task.objects.filter(pk=task.pk).exists())
