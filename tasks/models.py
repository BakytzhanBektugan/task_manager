from django.conf import settings
from django.db import models


class AbstractTask(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    file = models.FileField(upload_to='files/%Y/%m/%d/', null=True, blank=True)
    STATUS_CHOICES = (
        ('N', 'New'),
        ('P', 'Planned'),
        ('I', 'In progress'),
        ('C', 'Completed')
    )
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='N')
    completion_date = models.DateField(null=True, blank=True)

    class Meta:
        abstract = True


class Task(AbstractTask):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                              related_name='tasks')
    created = models.DateTimeField(auto_now_add=True)

    def save(self,  *args, **kwargs):
        task = super(Task, self).save()

        TaskHistory.objects.create(
            task=self,
            title=self.title,
            description=self.description,
            file=self.file,
            status=self.status,
            completion_date=self.completion_date
        )


class TaskHistory(AbstractTask):
    changed_at = models.DateTimeField(auto_now_add=True)
    task = models.ForeignKey(Task, on_delete=models.CASCADE,
                             related_name='task_history')

    class Meta:
        ordering = ['-changed_at']
