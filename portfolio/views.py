from django.shortcuts import render , get_object_or_404, redirect
from .models import Portfolio
from django.views.generic import ListView, DetailView, TemplateView
from .cart import Cart


class PortfolioListView(ListView):
    """This class represents a ListView for displaying portfolios.
    It sets the template name to 'home/index.html', specifies the context object name as 'portfolios',
    and sets pagination to display 9 portfolios per page."""

    template_name = 'home/index.html'
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
    

    
class PortfolioDetailView(DetailView):
    """This class represents a DetailView for displaying details of a portfolio.
    It sets the model to Portfolio, template name to 'home/portfolio-details.html',
    and context object name as 'portfolio'."""
    model = Portfolio
    template_name = 'home/portfolio-details.html'
    context_object_name = 'portfolio'

    
    def post(self, request, *args, **kwargs):
        """Handles POST requests for adding or removing portfolios from the cart."""
        cart = Cart(request)
        
        if 'id' in request.POST :
            product = get_object_or_404(Portfolio, id=int(request.POST['id']))    
            cart.delete_from_cart(product)
            
        else:
            product = get_object_or_404(Portfolio, id=int(request.POST['pk']))
            quantity = int(request.POST['quantity'])
            cart.add_to_cart_some_quantity(product, quantity)
            
        return redirect(request.path_info)



class PaymentView(TemplateView):
    template_name = 'home/cart.html'

    def post(self, request, *args, **kwargs):
        cart = Cart(request)
        cart.clear()
        return redirect(request.path_info)    