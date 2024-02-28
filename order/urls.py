from django.urls import path
from .views import CreateOrderByView


app_name = "order"

urlpatterns = [path("", CreateOrderByView.as_view(), name="order")]
