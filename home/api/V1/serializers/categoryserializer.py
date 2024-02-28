from rest_framework import serializers
from portfolio.models import Category
'''this class is for home category in api
'''
class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ["id", "name"]
