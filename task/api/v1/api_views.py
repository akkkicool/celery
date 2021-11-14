import sys

from rest_framework import filters, status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

import task.task
from task.api.v1.serializers import TaskSerializer
from task.models import Task

from configparser import ConfigParser, SafeConfigParser

parser = SafeConfigParser()
parser.read('config.ini')

class TaskViewSet(viewsets.ModelViewSet):
    """
    ModelViewSet Class for Task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class UpdateCronTime(APIView):

    def post(self, request):
        try:
            time = request.data['time']
            parser.set('cron','time',time)
            with open('config.ini', 'w+') as configfile:
                parser.write(configfile)
            return Response({'status': 200, 'message': 'Cron time updated', },
                            status.HTTP_200_OK)
        except Exception as error:
            return Response({'status': 500, 'message': 'Internal Server error', 'error': error.__str__()},
                            status.HTTP_500_INTERNAL_SERVER_ERROR)
