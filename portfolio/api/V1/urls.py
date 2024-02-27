from django.urls import path, include
from .views import *

from rest_framework.routers import DefaultRouter

app_name = 'api-v1'


urlpatterns = [
    path("portfolio/",PortfolioListView.as_view({'get': 'list', 'post':'create'}),name='courses'),
    path("portfolio/<int:pk>/",PortfolioDetailView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='portfolio-detail'),
    path("portfolio/",CategoryListView.as_view({'get': 'list', 'post':'create'}),name='courses'),
    path("portfolio/<int:pk>/",CategoryDetailView.as_view({'get': 'retrieve', 'put':'update','delete': 'destroy'}),name='portfolio-detail'),
]