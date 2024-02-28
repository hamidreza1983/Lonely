from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin,UpdateModelMixin, CreateModelMixin
from .serializer import SkillsSerializer
from home.models import Skills
from rest_framework.permissions import IsAuthenticated
'''created skils api with post put get and delet
'''
class SkillsListView (GenericAPIView, RetrieveModelMixin,
                      DestroyModelMixin,
                      CreateModelMixin, UpdateModelMixin):
    serializer_class =  SkillsSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Skills.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
