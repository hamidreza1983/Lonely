from django.urls import path
from .views import PortfolioListView, PortfolioDetailView

app_name = "api-v1"


urlpatterns = [
    path("portfolio/", PortfolioListView.as_view(), name="portfolio-list"),
    path("portfolio/<int:pk>/",
         PortfolioDetailView.as_view(),
         name="portfolio-detail"),
]
