from django.db import models
from django.contrib.auth.models import User

todo_choices = [
    ("todo", "Todo"),
    ("in_progress", "In progress"),
    ("on_hold", "On hold"),
    ("done", "Done"),
]

priotity_chioses = [
    (1, "High"),
    (2, "Medium"),
    (3, "Low"),
]


class Todo(models.Model):
    title = models.CharField(max_length=255, blank=True)
    content = models.TextField(blank=True)
    status = models.CharField(max_length=255, default="todo", choices=todo_choices)
    priority = models.CharField(
        max_length=255, default="todo", choices=priotity_chioses
    )
    owner = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned = models.ManyToManyField(User, related_name="assigned", default=owner)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="images/", blank=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.id} {self.title}"
