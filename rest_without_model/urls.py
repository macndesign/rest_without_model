# coding: utf-8
from __future__ import unicode_literals, absolute_import
from rest_framework import routers
from core.views import TaskViewSet


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet, base_name='tasks')
urlpatterns = router.urls
