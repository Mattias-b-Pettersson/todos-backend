from django.urls import path
from profiles import views

urlpatterns = [
    path("todos/", views.TodoList.as_view(), name="get_todos"),
    path("todo/<int:pk>/", views.TodoDetail.as_view(), name="get_todo"),
]
