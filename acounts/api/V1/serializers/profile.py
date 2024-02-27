from rest_framework import serializers
from django.shortcuts import get_object_or_404
from ...models import Profile
from ...models import CustomeUser

class ProfileSerializer(serializers.ModelSerializer):
    email = serializers.CharField(
        max_length=100,
        source="user.email",
        read_only=True)

    class Meta:
        model = Profile
        fields = ["id", "first_name", "last_name", "image", "email"]


class ResendEmailSerializer(serializers.Serializer):
    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs