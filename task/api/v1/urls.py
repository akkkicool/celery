"""
Claims API V1
"""
from rest_framework import routers

from task.api.v1.api_views import TaskViewSet

task_router = routers.DefaultRouter()
task_router.register(r'task', TaskViewSet)