from django.views.generic import TemplateView

class ResetPasswordDoneView(TemplateView):
    '''
    this class is used for show a meesage after sending email for rest password
    '''
    template_name = "registration/resetpassword_done.html"
