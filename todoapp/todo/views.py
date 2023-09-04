from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.contrib import messages
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.db.models import Q




# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'tasks.html'

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('query')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(description__icontains=query))
        return queryset

class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'task_detail.html'

class TaskCreate(CreateView):
    model = Task
    fields = ['title','description','completed']
    template_name = 'add_task.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.success(self.request, "The tas was created successfully.")
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model= Task
    fields = ['title','description','completed']
    template_name = 'update_task.html'
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdate,self).form_valid(form)
    



class TaskDelete(LoginRequiredMixin,DeleteView):
    model= Task
    template_name = 'delete_task.html'
    success_url = reverse_lazy('tasks')

def form_valid(self, form):
    #is used to check whether the current HTTP request is an AJAX request or not.
    if self.request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        # Handle htmx request
        messages.success(self.request, "The task was deleted successfully.")
        return JsonResponse({'message': 'Success'})
    else:
        # Handle non-htmx request as before
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete, self).form_valid(form)




    
