from rest_framework import serializers
from .models import Todo
from django.utils import timezone


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.id")
    profile_image = serializers.ReadOnlyField(source="owner.image")
    due_date_has_passed = serializers.SerializerMethodField()
    assigned_username = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    def get_status(self, obj):
        if obj.status == "on_hold":
            return "On Hold"
        elif obj.status == "in_progress":
            return "In Progress"
        elif obj.status == "done":
            return "Done"
        elif obj.status == "todo":
            return "Todo"
        else:
            return obj.status

    def get_assigned_username(self, obj):
        return obj.assigned.values_list("username", flat=True)

    def get_is_owner(self, obj):
        request = self.context["request"]
        return request.user == obj.owner

    def get_due_date_has_passed(self, obj):
        return obj.due_date < timezone.now()
    
    class Meta:
        model = Todo
        fields = [
            "id",
            "owner",
            "created_at",
            "updated_at",
            "title",
            "status",
            "content",
            "priority",
            "is_owner",
            "file",
            "assigned",
            "assigned_username",
            "profile_id",
            "profile_image",
            "due_date",
            "due_date_has_passed",
        ]
