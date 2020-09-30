from rest_framework import serializers
from tasks.models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('owner', )


class TaskHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskHistory
        fields = '__all__'
