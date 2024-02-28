from ..models import CustomeUser
from django.shortcuts import get_object_or_404
from ..forms import ResetpasswordConfirm
from django.views.generic import FormView
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions

class PasswordResetConfirmView(FormView):
    form_class = ResetpasswordConfirm
    success_url = "/accounts/reset/done/"
    template_name = "registration/resetpassword_confirm.html"

    def form_valid(self, form):
        user_data = AccessToken(self.kwargs.get("token"))
        user_id = user_data["user_id"]
        user = get_object_or_404(CustomeUser, id=user_id)
        password1 = self.request.POST.get("new_password1")
        password2 = self.request.POST.get("new_password2")

        if password1 != password2:
            raise ValueError({"detail": "password dose not confirmed"})

        try:

            validate_password(password1)

        except exceptions.ValidationError as e:

            raise ValueError({"detail": list(e.messages)})
        
        user.set_password(password1)
        user.save()


        
        return super().form_valid(form)
    
   