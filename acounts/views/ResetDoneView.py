
from django.views.generic import TemplateView


class ResetDoneView(TemplateView):
    template_name = "registration/resetpassword_complete.html"