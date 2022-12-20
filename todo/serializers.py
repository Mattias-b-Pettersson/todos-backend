from rest_framework import serializers
from .models import Todo
from profiles.models import Profile
from django.utils import timezone


class TodoSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.username")
    is_owner_or_assigned = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source="owner.id")
    profile_image = serializers.ReadOnlyField(source="owner.image")
    due_date_has_passed = serializers.SerializerMethodField()
    assigned_username_id_img = serializers.SerializerMethodField()
    status_prettified = serializers.SerializerMethodField()

    def status_prettified(self, obj):
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

    def get_assigned_username_id_img(self, obj):
        username = obj.assigned.values_list("username", flat=True)
        id = obj.assigned.values_list("id", flat=True)
        img = []
        for i in id:
            img.append(Profile.objects.get(id=i).image.url)
        print(img)

        return zip(username, img, id)

    def get_is_owner_or_assigned(self, obj):
        request = self.context["request"]
        return obj.owner == request.user or obj.assigned.filter(id=request.user.id).exists()

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
            "status_prettified",
            "content",
            "priority",
            "is_owner_or_assigned",
            "file",
            "assigned",
            "assigned_username_id_img",
            "profile_id",
            "profile_image",
            "due_date",
            "due_date_has_passed",
        ]
