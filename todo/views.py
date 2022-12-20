# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from core.permissions import IsOwnerOrAssignedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    """
    List all todos.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.filter()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "owner",
        "assigned",
        "status",
        "priority",
    ]
    search_fields = {
        "title",
        "priority",
        "status",
    }

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def post(self, request, *args, **kwargs):
        print(request.data)
        return self.create(request, *args, **kwargs)


class TodoDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """

    permission_classes = [IsOwnerOrAssignedOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
