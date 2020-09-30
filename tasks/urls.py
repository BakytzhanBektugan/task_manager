from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework import renderers


task_list = views.TaskViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

task_detail = views.TaskViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

urlpatterns = [
    path('tasks/', task_list, name='tasks_list'),
    path('tasks/<int:pk>/', task_detail, name='task_detail'),
]
