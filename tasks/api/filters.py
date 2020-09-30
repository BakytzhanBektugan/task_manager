from django_filters import rest_framework as filters
from tasks.models import Task


STATUS_CHOICES = (
        ('N', 'New'),
        ('P', 'Planned'),
        ('I', 'In progress'),
        ('C', 'Completed')
    )


class TasksFilter(filters.FilterSet):
    status = filters.ChoiceFilter(choices=STATUS_CHOICES)
    completion_date = filters.DateFilter(lookup_expr='lte')

    class Meta:
        model = Task
        fields = ['status', 'completion_date',]
