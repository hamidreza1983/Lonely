from django.urls import path
from home.views import home, portfolio_details

app_name = 'home'
urlpatterns = [
    path("", home, name="home"),
    path(
        "portfolio-details/<int:id>",
        portfolio_details,
        name="portfolio-dretails",
    ),
]
