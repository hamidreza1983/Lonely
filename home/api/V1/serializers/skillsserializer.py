from rest_framework import serializers
from home.models import Skills
'''
this class make skills api in home
'''
class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ["id", "name"]
