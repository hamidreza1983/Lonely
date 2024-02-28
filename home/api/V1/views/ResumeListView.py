from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from home.api.V1.serializers import  ResumeSerializer
from home.models import Resume
from rest_framework.permissions import IsAuthenticated

class ResumeListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    '''resume api view with permisson
    '''
    serializer_class =  ResumeSerializer
    permission_classes = [IsAuthenticated]

    
    def get_queryset(self):
        return Resume.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
