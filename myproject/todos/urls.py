from django.urls import path
from .views import TodoListView, TodoDetailView, TodoUpdateView, TodoDeleteView

urlpatterns = [
    path("", TodoListView.as_view(), name="todo_list"),
    path("todos/<int:pk>", TodoDetailView.as_view(), name="todo_detail"),
    path("todos/<int:pk>/edit", TodoUpdateView.as_view(), name="todo_edit"),
    path("todos/<int:pk>/delete", TodoDeleteView.as_view(), name="todo_delete")
]
