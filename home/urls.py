from django.urls import path, include
from home.views import home, portfolio_details

app_name = 'home'
urlpatterns = [
    path("", home, name="home"),
    path(
        "portfolio-details/<int:id>",
        portfolio_details,
        name="portfolio-dretails",
    ),
    path("api/V1/", include("home.api.V1.urls")),
]
