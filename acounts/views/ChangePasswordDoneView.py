from django.views.generic import TemplateView

 
class ChangePasswordDoneView(TemplateView):
    '''
    this class is after changing password
    '''
    template_name = "registration/changepassword_done.html"