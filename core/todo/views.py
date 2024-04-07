from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import *
# Create your views here.

class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'  # we have overwritten the default context_object_name attribute to tasks

class GetTask(DetailView):
    model = Task
    template_name = 'todo/task.html'  # overwriting the default template_name attribute to task.html
    context_object_name = 'task'


class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')

class DeleteTask(DeleteView):
    model = Task
    template_name = 'todo/delete_task.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')