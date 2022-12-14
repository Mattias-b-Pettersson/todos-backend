from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """

    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.profile.id")
    profile_image = serializers.ReadOnlyField(source="owner.profile.image.url")
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        """
        Checks if the user is the owner of the comment.
        """
        request = self.context["request"]
        return request.user == obj.owner

    def get_updated_at(self, obj):
        """
        Returns a natural time representation of the updated_at field.
        """
        return naturaltime(obj.updated_at)

    def get_created_at(self, obj):
        """
        Returns a natural time representation of the created_at field.
        """
        return naturaltime(obj.created_at)

    class Meta:
        model = Comment
        fields = [
            "id",
            "owner",
            "is_owner",
            "profile_id",
            "profile_image",
            "todo",
            "created_at",
            "updated_at",
            "content",
        ]


class CommentDetailSerializer(CommentSerializer):
    todo = serializers.ReadOnlyField(source="todo.id")
