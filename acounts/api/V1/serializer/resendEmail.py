from rest_framework import serializers
from django.shortcuts import get_object_or_404
from acounts.models import CustomeUser

class ResendEmailSerializer(serializers.Serializer):
    '''
    this class resend email for user
    '''
    email = serializers.CharField(label=("Email"), write_only=True)

    def validate(self, attrs):
        '''this function check user email'''
        user = get_object_or_404(CustomeUser, email=attrs.get("email"))
        attrs["user"] = user
        return attrs