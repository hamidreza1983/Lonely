from ..forms import PasswordChangeForm 
from django.views.generic import FormView
from django.contrib.auth.mixins import LoginRequiredMixin



class ChangePasswordView(LoginRequiredMixin, FormView):
    template_name = "registration/changepassword_form.html"
    form_class = PasswordChangeForm
    success_url = "/accounts/change-password/done/"
    

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.request.user
        return kwargs
    
    def form_valid(self, form):
        form.save()
        # Updating the password logs out all other sessions for the user
        # except the current one.
        return super().form_valid(form)