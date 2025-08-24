from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from .models import Todo, Category
from .forms import TodoForm

# Create your views here.
class TodoListView(LoginRequiredMixin, ListView):
    model = Todo
    template_name = 'todos/index.html'
    context_object_name = 'todos'
    def get_queryset(self):
        user = self.request.user
        queryset = Todo.objects.filter(
            Q(user=user) | Q(group__in=user.todo_groups.all())
        )
        category_id = self.request.GET.get('category')
        if category_id:
            queryset = queryset.filter(category_id=category_id)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context

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
