from django.urls import path, include
from .views import *


app_name = 'portfolios'

urlpatterns = [
    path("", PortfolioListView.as_view(),name='portfolios'),
    path("category/<str:cat>",PortfolioListView.as_view(),name="portfolio_cat"),
    path("portfolio-detail/<int:pk>",PortfolioDetailView.as_view(),name="portfolio_detail"),
    path("payment",PaymentView.as_view(),name="cart"),
    path("api/V1/",include('portfolio.api.V1.urls')),
]


