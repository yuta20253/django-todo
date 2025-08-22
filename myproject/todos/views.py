from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Todo
from .forms import TodoForm

# Create your views here.
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/index.html'
    context_object_name = 'todos'

class TodoDetailView(LoginRequiredMixin, DetailView):
    model = Todo
    template_name = 'todos/detail.html'
    context_object_name = 'todo'

class TodoUpdateView(LoginRequiredMixin, UpdateView):
    model = Todo
    form_class = TodoForm
    template_name = 'todos/form.html'
    success_url = reverse_lazy('todo_list')

class TodoDeleteView(LoginRequiredMixin, DeleteView):
    model = Todo
    template_name = 'todos/confirm_delete.html'
    success_url = reverse_lazy('todo_list')
