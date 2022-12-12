# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from core.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Todo
from .serializers import ProfileSerializer


class TodoList(generics.ListCreateAPIView):
    """
    List all todos.
    """

    queryset = Todo.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    filterset_fields = ["owner", "assigned"]
    search_fields = {
        "title",
        "priority",
        "status",
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """

    permission_classes = [IsOwnerOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = ProfileSerializer
