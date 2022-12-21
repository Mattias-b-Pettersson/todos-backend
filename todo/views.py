# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters, permissions
from core.permissions import IsOwnerOrAssignedOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from .models import Todo
from .serializers import TodoSerializer


class TodoList(generics.ListCreateAPIView):
    """
    List all todos, or create a new todo.  
    Search by title, priority, status and also filter by owner, assigned, status, priority.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Todo.objects.filter()
    serializer_class = TodoSerializer
    filter_backends = [filters.SearchFilter,
                       DjangoFilterBackend, filters.OrderingFilter]
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
    Retrieve, update or delete a todo instance if the user is the owner or is assigned to the todo.
    """

    permission_classes = [IsOwnerOrAssignedOrReadOnly]
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
