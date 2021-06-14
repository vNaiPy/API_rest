from rest_framework import status
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import viewsets

from app.models import Todo
from app.serializers import TodoSerializer

class TodoViewSet(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

