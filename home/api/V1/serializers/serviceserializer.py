from rest_framework import serializers
from home.models import Services
from .categoryserializer import CategorySerializer
'''this class is for service serializer in home
'''
class ServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = ["title", "content", "category","image", 'status']
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category,
                                                many=True).data
        return rep


    
    
