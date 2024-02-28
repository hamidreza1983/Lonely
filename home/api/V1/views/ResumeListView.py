from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from .serializer import  ResumeSerializer
from home.models import Resume



class ResumeListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    serializer_class =  ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(status=True)
    def put(self, request, *args, **kwargs):
         return self.update(request, *args, **kwargs) 
    def delete(self, request, *args, **kwargs):
         return self.destroy(request, *args, **kwargs)
