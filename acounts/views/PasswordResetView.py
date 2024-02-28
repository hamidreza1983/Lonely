from ..models import CustomeUser
from django.shortcuts import get_object_or_404
from ..forms import  ResetpasswordEmail
from django.views.generic import FormView
from rest_framework_simplejwt.tokens import RefreshToken
from mail_templated import EmailMessage
from ..multi_threading import SendEmailWithThreading


class PasswordResetView(FormView):
    '''
    This class is for getting gmail for reset password process
    '''
    form_class = ResetpasswordEmail
    success_url = "/accounts/resetPassword/done/"
    template_name = "registration/resetpassword_form.html"


    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token) 
    
    def form_valid(self, form):
        email = self.request.POST.get('email')
        user = get_object_or_404(CustomeUser, email=email)


        token = self.get_tokens_for_user(user)
        
        message = EmailMessage(
            "registration/resetpassword_email.html",
            {"token": token},
            "admin@hesam.com",
            to=[email],
        )
        email = SendEmailWithThreading(message)
        email.start()
        return super().form_valid(form)
    