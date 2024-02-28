from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from .serializer import ResumeSerializer
from home.models import Resume

class ResumeDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):
    serializer_class =  ResumeSerializer

    def get_queryset(self):
        return Resume.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
 