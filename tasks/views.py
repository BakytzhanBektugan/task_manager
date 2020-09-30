from rest_framework import generics, viewsets, permissions
from .models import Task
from .api.serializers import TaskSerializer
from .api.permissions import IsOwnerOnly
from django_filters.rest_framework import DjangoFilterBackend
from .api.filters import TasksFilter


class TaskViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing task instances.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOnly]
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (DjangoFilterBackend, )
    filterset_class = TasksFilter

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(owner_id=self.request.user.id)
