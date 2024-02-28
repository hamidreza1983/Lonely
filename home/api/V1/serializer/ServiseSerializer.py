from rest_framework import serializers
from home.models import Services






class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ["title", "content", "category","image", 'status']


    
    
