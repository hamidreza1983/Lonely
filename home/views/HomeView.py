
from django.views.generic import TemplateView
from portfolio.models import Portfolio,Category
class HomeView(TemplateView):
    template_name = 'home/index.html'
    model=[Portfolio,Category]