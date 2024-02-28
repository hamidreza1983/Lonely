
from django.views.generic import TemplateView


class ResetDoneView(TemplateView):
    '''
    When reset password process is completely done
    '''
    template_name = "registration/resetpassword_complete.html"