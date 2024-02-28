from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .serializer import CategorySerializer
from home.models import Services
class CategoryListView(GenericAPIView, ListModelMixin, CreateModelMixin):   
    serializer_class =  CategorySerializer
    
    def get_queryset(self):
        return Services.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    