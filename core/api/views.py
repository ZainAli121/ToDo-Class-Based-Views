from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from django.contrib.auth.models import User

from todo.models import *
from .serializers import *

# api view for signup
class SignUpView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class TasksViewCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # allow task to be saved with the user who is logged in
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    # get only the tasks of the logged in user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)


class TaskViewUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    # get only the task of the logged in user
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)
    

class Serach(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = super().get_queryset().filter(user=self.request.user)
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(title__startswith=search_query)
            return queryset