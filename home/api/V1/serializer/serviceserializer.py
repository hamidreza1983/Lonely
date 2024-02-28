from rest_framework import serializers
from home.models import Services
class ServiceSerializer(serializers.ModelSerializer):
    '''
    this class is for service serializer in home
    '''
    class Meta:
        model = Services
        fields = ["title", "content", "category","image", 'status']


    
    
