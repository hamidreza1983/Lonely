from rest_framework import serializers
from home.models import Skills



class SkillsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Skills
        fields = ["id", "name"]
