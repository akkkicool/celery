from rest_framework import serializers


from task.models import Task


class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model
    """

    class Meta(object):
        model = Task
        fields = '__all__'

