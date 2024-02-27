from django.urls import path, include
from .views import *


app_name = 'courses'

urlpatterns = [
    path("", PortfolioListView.as_view(),name='courses'),
    path("category/<str:cat>",PortfolioListView.as_view(),name="course_cat"),
    path("teacher/<str:teacher>",PortfolioListView.as_view(),name="course_teacher"),
    path("search/",PortfolioListView.as_view(),name="course_search"),
    path("course-detail/<int:pk>",PortfolioDetailView.as_view(),name="course_detail"),
    path("payment",PaymentView.as_view(),name="cart"),
    path("payment",PaymentView.as_view(),name="cart"),
    path("api/V1/",include('courses.api.V1.urls')),
]


