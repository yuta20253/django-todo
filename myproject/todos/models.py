from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Group(models.Model):
    name = models.CharField(max_length=50, null=False)
    members = models.ManyToManyField(User, related_name="todo_groups")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=30, null=False)

class Todo(models.Model):

    PRIORITY_CHOICES = [
        (1, "高"),
        (2, "中"),
        (3, "低")
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.CharField(max_length=30, null=False)
    description = models.TextField(null=True, blank=True)
    is_completed = models.BooleanField(default=False)
    due_date = models.DateField(null=False)
    priority = models.IntegerField(choices=PRIORITY_CHOICES, default=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def is_group_task(self):
        return self.group is not None

    def __str__(self):
        return self.title
