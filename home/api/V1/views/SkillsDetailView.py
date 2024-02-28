from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    DestroyModelMixin, 
    RetrieveModelMixin,
    UpdateModelMixin, 
    CreateModelMixin,
    ListModelMixin
)
from rest_framework.permissions import IsAuthenticated
from home.api.V1.serializer import SkillsSerializer
from home.models import Skills


class SkillsDetailView (
    GenericAPIView, 
    RetrieveModelMixin,
    DestroyModelMixin,
    CreateModelMixin, 
    UpdateModelMixin,
    ListModelMixin
    ):
    '''
    this class is skills for api
    '''
    serializer_class =  SkillsSerializer
    permission_classes = [IsAuthenticated]


    def get_queryset(self):
        return Skills.objects.all()

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    