from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (
    DestroyModelMixin,
    RetrieveModelMixin,
    UpdateModelMixin,
)

from ....models import Portfolio
from ..serializer import PortfolioApiSerializer


class PortfolioDetailView(
    GenericAPIView, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin
):
    serializer_class = PortfolioApiSerializer

    def get_queryset(self):
        return Portfolio.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
