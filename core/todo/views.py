from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login


from .models import *
# Create your views here.

class LoginUser(LoginView):
    template_name = 'todo/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterUser(FormView):
    template_name = 'todo/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterUser, self).form_valid(form)
    
    # overwriting the default get method to redirect the user to the tasks page if they are already authenticated
    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterUser, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'  # we have overwritten the default context_object_name attribute to tasks

    # overwriting the default get_queryset method to filter the tasks based on the user
    # each user will only see their tasks
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(comeplete=False).count()

        # search
        search_input = self.request.GET.get('search') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(title__startswith=search_input)

        context['search_input'] = search_input

        return context
    

class GetTask(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'todo/task.html'  # overwriting the default template_name attribute to task.html
    context_object_name = 'task'


class CreateTask(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'desc', 'comeplete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
    

class UpdateTask(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'desc', 'comeplete']
    success_url = reverse_lazy('tasks')


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    template_name = 'todo/delete_task.html'
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')