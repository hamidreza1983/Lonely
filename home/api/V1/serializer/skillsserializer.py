from rest_framework import serializers
from home.models import Skills

class SkillsSerializer(serializers.ModelSerializer):
   '''
   this class make skills api in home
   '''
   class Meta:
      model = Skills
      fields = ["id", "name","percent"] 
  
