from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin, CreateModelMixin
from .serializer import ServiceSerializer
from home.models import Services
from rest_framework.permissions import IsAuthenticated

class ServicesDetailView(GenericAPIView, CreateModelMixin,
                         DestroyModelMixin, UpdateModelMixin):
    '''
    this view is for detail services
    '''
    serializer_class = ServiceSerializer
    permission_classes =[IsAuthenticated]

    def get_queryset(self):
        return Services.objects.filter(status=True)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
 