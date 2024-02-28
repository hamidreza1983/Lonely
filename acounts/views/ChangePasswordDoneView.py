from django.views.generic import TemplateView

 
class ChangePasswordDoneView(TemplateView):
    template_name = "registration/changepassword_done.html"