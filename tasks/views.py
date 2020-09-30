from django.http import JsonResponse
from rest_framework import generics, viewsets, permissions, views
from rest_framework.response import Response

from .models import Task, TaskHistory
from .api.serializers import TaskSerializer, TaskHistorySerializer
from .api.permissions import IsOwnerOnly
from django_filters.rest_framework import DjangoFilterBackend
from .api.filters import TasksFilter


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances.
    """
    permission_classes = [IsOwnerOnly, ]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TasksFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner_id=self.request.user.id)


class TaskHistoryView(views.APIView):

    def get(self, request, pk):
        queryset = TaskHistory.objects.filter(task_id=pk).filter(task__owner=request.user)
        serializer = TaskHistorySerializer(queryset, many=True)
        return JsonResponse(serializer.data, safe=False)
