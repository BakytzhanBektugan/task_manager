from django.urls import path
from . import views


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
    path('tasks/<int:pk>/history/', views.TaskHistoryView.as_view(), name='task_history'),
]
