from ..models import Portfolio
from ..cart import Cart
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import DetailView


class PortfolioDetailView(DetailView):
    """This class represents a DetailView
       for displaying details of a portfolio.
       It sets the model to Portfolio,
       template name to 'home/portfolio-details.html',
       and context object name as 'portfolio'."""

    model = Portfolio
    template_name = "home/portfolio-details.html"
    context_object_name = "portfolio"

    def post(self, request, *args, **kwargs):
        """Handles POST requests for adding or
        removing portfolios from the cart."""
        cart = Cart(request)

        if "id" in request.POST:
            product = get_object_or_404(Portfolio, id=int(request.POST["id"]))
            cart.delete_from_cart(product)

        else:
            product = get_object_or_404(Portfolio, id=int(request.POST["pk"]))
            quantity = int(request.POST["quantity"])
            cart.add_to_cart_some_quantity(product, quantity)

        return redirect(request.path_info)
