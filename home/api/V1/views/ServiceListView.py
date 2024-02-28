from rest_framework.generics import GenericAPIView 
from rest_framework.mixins import CreateModelMixin,ListModelMixin
from home.api.V1.serializers import ServiceSerializer
from home.models import Services
from rest_framework.permissions import IsAuthenticated

class ServicesListView(GenericAPIView, ListModelMixin, CreateModelMixin):
    '''api for services with method get 
    and permissoin classs_isaythenticated
    '''
    serializer_class = ServiceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Services.objects.filter(status=True)
 