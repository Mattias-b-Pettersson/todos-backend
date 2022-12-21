from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model,
    adds an extra field when returning a list of Profile instances.
    """
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Returns True if the user is the owner of the profile.
        """
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Profile
        fields = [
            "id", "owner", "created_at", "updated_at",
            "name", "content", "image", "is_owner",
        ]
