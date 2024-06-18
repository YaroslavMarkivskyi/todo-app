"""
Tests for the group API.
"""
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status

from todo.serializers import GroupSerializer

from todo.models import Group


GROUPS_URL = reverse('todo:group-list')


def detail_url(group_id):
    """Create and return an group detail URL."""
    return reverse('todo:group-detail', args=[group_id])


def create_user(email='user@example.com', password='testpass123'):
    """Create return user."""
    return get_user_model().objects.create_user(email=email, password=password)


class PublicGroupsApiTests(TestCase):
    """Test unauthenticated API requests."""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required for retrieving groups."""
        res = self.client.get(GROUPS_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateGroupsApiTests(TestCase):
    """Test unauthenticated API requests."""
    def setUp(self):
        self.user = create_user()
        self.client = APIClient()
        self.client.force_authenticate(self.user)

    def test_retrieve_groups(self):
        """Test retrieving a list of groups."""
        Group.objects.create(user=self.user, title='Kale')
        Group.objects.create(user=self.user, title='Vanilla')
        res = self.client.get(GROUPS_URL)

        groups = Group.objects.all().order_by('-title')
        serializer = GroupSerializer(groups, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_groups_limited_to_user(self):
        """Test list of groups is limited to authenticated user."""
        user2 = create_user(email='user2@example.com')
        Group.objects.create(user=user2, title='Salt')
        group = Group.objects.create(user=self.user, title='Pepper')

        res = self.client.get(GROUPS_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['title'], group.title)
        self.assertEqual(res.data[0]['id'], group.id)

    def test_update_group(self):
        """Test updating an group."""
        group = Group.objects.create(user=self.user, title='Cilantro')

        payload = {'title': 'Coriander'}
        url = detail_url(group.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        group.refresh_from_db()
        self.assertEqual(group.title, payload['title'])

    def test_delete_group(self):
        """Test deleting an group."""
        group = Group.objects.create(user=self.user, title='Lettuce')

        url = detail_url(group.id)
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        groups = Group.objects.filter(user=self.user)
        self.assertFalse(groups.exists())
