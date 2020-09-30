from rest_framework import serializers
from tasks.models import Task, TaskHistory


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        exclude = ('owner', )
        read_only_fields = ('owner',)


class TaskHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TaskHistory
        fields = '__all__'
