from django.views.generic import TemplateView

class ResetPasswordDoneView(TemplateView):
    template_name = "registration/resetpassword_done.html"
