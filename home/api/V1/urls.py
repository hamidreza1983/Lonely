from django.urls import path
from home.api.V1.views.CategoryListView import CategoryListView
from home.api.V1.views.ServicesListView import ServicesListView
from home.api.V1.views.ServiceDetailView import ServiceDetailView
from home.api.V1.views.ResumeListView import ResumeListView
from home.api.V1.views.SkillsListView import SkillsListView
from home.api.V1.views.ResumeDetailView import ResumeDetailView

app_name = 'api-v1'

urlpatterns = [
    path("home/",CategoryListView.as_view(),name='category'),
    path("home/",ServicesListView.as_view(),name='services'),
    path("home/<int:pk>",ServiceDetailView.as_view(),name='service_detail'),
    path("home/",ResumeListView.as_view(),name='resume'),
    path("home/<int:pk>",ResumeDetailView.as_view(),name='resume'),
    path("home/",SkillsListView.as_view(),name='skills'),



]