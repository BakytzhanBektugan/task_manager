from django.conf import settings
from django.db import models


class Task(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='tasks')
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=300)
    file = models.FileField(upload_to='files/%Y/%m/%d/', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('N', 'New'),
        ('P', 'Planned'),
        ('I', 'In progress'),
        ('C', 'Completed')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    completion_date = models.DateField(null=True, blank=True)
