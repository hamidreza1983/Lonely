
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.permissions import IsAdminUser, IsAuthenticated, IsAuthenticatedOrReadOnly
from .serializer import *
from ...models import *
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView , ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView
from rest_framework.mixins import CreateModelMixin, DestroyModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import viewsets
from .permission import IsAdminOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginator import CustomePaginate

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
