from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from .serializer import PortfolioApiSerializer
from ...models import Portfolio
class CategoryListView(GenericAPIView, ListModelMixin, CreateModelMixin):   
    serializer_class = PortfolioApiSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    