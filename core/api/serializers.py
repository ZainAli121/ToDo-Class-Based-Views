from rest_framework import serializers
from django.contrib.auth.models import User
from todo.models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

        def create(self, validate_data):
            user = User.objects.create_user(**validate_data)
            return user


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

