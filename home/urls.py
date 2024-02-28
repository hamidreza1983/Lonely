from django.urls import path, include
from home.views import HomeView
from portfolio.views import PortfolioListView
app_name = 'home'
urlpatterns = [
    path("", HomeView.as_view(),name="home"),
    path("api/V1/", include("home.api.V1.urls")),
]
