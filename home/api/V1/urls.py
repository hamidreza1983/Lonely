from django.urls import path
from home.api.V1.views import (
    ServicesListView,
    ServicesDetailView,
    ResumeListView,
    SkillsListView,
    SkillsDetailView
)




app_name = 'api-v1'

urlpatterns = [
    path("services/",ServicesListView.as_view(),name='services'),
    path("service/<int:pk>",ServicesDetailView.as_view(),name='service_detail'),
    path("resume/",ResumeListView.as_view(),name='resume'),
    path("skill/",SkillsListView.as_view(),name='skills'),
    path("skill/<int:pk>",SkillsDetailView.as_view(),name='skills'),

]