"""
URL mappings for the recipe app.
"""
from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from todo import views


router = DefaultRouter()
router.register('tasks', views.TaskViewSet)
router.register('groups', views.GroupViewSet)

app_name = 'todo'

urlpatterns = [
    path('', include(router.urls)),
]
