from ..cart import Cart
from django.shortcuts import redirect
from django.views.generic import TemplateView


class PaymentView(TemplateView):
    """This class represents a TemplateView for handling payments.
    It sets the template name to 'home/cart.html'.
    template_name = 'home/cart.html'"""

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests for clearing the cart after payment.
        """
        cart = Cart(request)
        cart.clear()
        return redirect(request.path_info)
