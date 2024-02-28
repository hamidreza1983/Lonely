from rest_framework import serializers
from home.models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    '''this class maked resume api 
'''
    class Meta:
        model = Resume
        fields = ["title", "content", "location","year", "phone", "email" ,"status"]

   
    