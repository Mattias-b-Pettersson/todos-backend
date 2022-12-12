from rest_framework import serializers
from .models import Todo


class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.id")
    profile_image = serializers.ReadOnlyField(source="owner.image")

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    class Meta:
        model = Todo
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "title",
            "content",
            "priority",
            "is_owner",
            "file",
            "assigned",
            "profile_id",
            "profile_image",
        ]
