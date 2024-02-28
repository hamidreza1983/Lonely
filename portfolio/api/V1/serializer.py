from rest_framework import serializers
from ...models import *
from acounts.models import CustomeUser


class PortfolioApiSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=200)
    price = serializers.IntegerField()

    class Meta:
        model = Portfolio
        fields = ["title", "price", "content", "category", "client", "image", 'status']

    
    def detail(self,obj):
        request = self.context.get('request')
        return request.build_absolute_uri(obj.id)
    

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['category'] = CategorySerializer(instance.category, many=True).data
        request = self.context.get('request')
        kwargs = request.parser_context.get('kwargs')
        if kwargs.get('pk') is not None:
            rep.pop('content')
        return rep
    
    def create(self, validated_data):
        validated_data['content'] = 'for this portfolio'
        return super().create(validated_data)

    

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]


        