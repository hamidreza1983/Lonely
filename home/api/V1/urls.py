from django.urls import path
from home.api.V1.views.ServiceListView import ServicesListView
from home.api.V1.views.ServiceDetailView import ServicesDetailView
from home.api.V1.views.ResumeListView import ResumeListView
from home.api.V1.views.SkillsListView import SkillsListView

app_name = 'api-v1'

urlpatterns = [
    path("home/",ServicesListView.as_view(),name='services'),
    path("home/<int:pk>",ServicesDetailView.as_view(),name='service_detail'),
    path("home/",ResumeListView.as_view(),name='resume'),
    path("home/",SkillsListView.as_view(),name='skills'),



]