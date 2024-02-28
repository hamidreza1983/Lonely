from ..models import Portfolio
from ..views import PortfolioDetailView
from django.views.generic import ListView

class PortfolioListView(ListView):
    """This class represents a ListView for displaying portfolios.
    It sets the template name to 'home/index.html', specifies the context object name as 'portfolios',
    and sets pagination to display 9 portfolios per page."""

    template_name = 'portfolio/portfolio.html'
    context_object_name = 'portfolios'
    paginate_by = 9

    def get_queryset(self):
        """"Returns the queryset of portfolios based on the category specified in the URL kwargs."""
        if self.kwargs.get('cat'):
            return Portfolio.objects.filter(category__name=self.kwargs.get('cat'))
        else:
            return Portfolio.objects.filter(status=True) 
    def post(self, request, *args, **kwargs):
        """Handles POST requests by delegating the handling to PortfolioDetailView."""
        post_detail = PortfolioDetailView()
        return post_detail.post(request,*args,**kwargs)