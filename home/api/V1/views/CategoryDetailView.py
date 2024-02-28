from rest_framework.generics import GenericAPIView
from rest_framework.mixins import DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from ..serializer import CategorySerializer
from ....models import Services
class CategoryDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):   
    serializer_class = CategorySerializer

    def get_queryset(self):
        return Services.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)