from django.db.models import Count
# from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from core.permissions import IsOwnerOrReadOnly
from .models import Profile
from .serializers import ProfileSerializer


class ProfileList(generics.ListAPIView):
    """
    List all profiles.
    No create view as profile creation is handled by django signals.
    """
    queryset = Profile.objects.all()
    # queryset = Profile.objects.annotate(
    #     posts_count=Count("owner__post", distinct=True),
    #     followers_count=Count("owner__followed", distinct=True),
    #     following_count=Count("owner__following", distinct=True)
    # ).order_by("-created_at")
    serializer_class = ProfileSerializer
    # filter_backends = [
    #     filters.OrderingFilter,
    #     filters.SearchFilter,
    #     DjangoFilterBackend
    # ]
    # filterset_fields = [
    #     "owner__following__followed__profile"
    # ]
    # ordering_fields = [

    # ]


class ProfileDetail(generics.RetrieveUpdateAPIView):
    """
    Retrieve or update a profile if you're the owner.
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
