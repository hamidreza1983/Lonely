from .serializer import *
from ...models import *
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin

class PortfolioDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):   
    #queryset = Course.objects.filter(status=True)
    serializer_class = PortfolioSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    

class PortfolioListView(GenericAPIView, ListModelMixin, CreateModelMixin):   
    #queryset = Course.objects.filter(status=True)
    serializer_class = PortfolioApiSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class CategoryDetailView(GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin):   
    #queryset = Course.objects.filter(status=True)
    serializer_class = PortfolioApiSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
class CategoryListView(GenericAPIView, ListModelMixin, CreateModelMixin):   
    #queryset = Course.objects.filter(status=True)
    serializer_class = PortfolioApiSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
