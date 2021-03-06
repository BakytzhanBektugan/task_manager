from django_filters import rest_framework as filters
from tasks.models import Task


STATUS_CHOICES = (
        ('N', 'New'),
        ('P', 'Planned'),
        ('I', 'In progress'),
        ('C', 'Completed')
    )


class TasksFilter(filters.FilterSet):
    """
    Фильтрация Task по статусу и запланированной дате завершения
    """
    status = filters.ChoiceFilter(choices=STATUS_CHOICES)
    completion_date = filters.DateFilter(field_name='completion_date')
    completion_date_from = filters.DateFilter(field_name='completion_date', lookup_expr='gte')
    completion_date_to = filters.DateFilter(field_name='completion_date', lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['status', 'completion_date',]
