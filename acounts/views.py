from .models import CustomeUser
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import (
    AuthenticationForm,
    CustomUserCreation,
    PasswordChangeForm, 
    ResetpasswordEmail,
    ResetpasswordConfirm
)
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from mail_templated import EmailMessage
from .multi_threading import SendEmailWithThreading
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions


class LoginView(FormView):
    template_name = "registration/login.html"
    form_class = AuthenticationForm
    success_url = "/"

    def form_valid(self, form):
        email = self.request.POST.get("email")
        password = self.request.POST.get("password")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return super().form_valid(form)


class LogOutView(TemplateView):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect("/")


class SignUpView(CreateView):
    template_name = "registration/signup.html"
    form_class = CustomUserCreation
    success_url = "/accounts/login/"  #'registration/login'

    def form_valid(self, form):
        form.save()
        email = self.request.POST.get("email")
        password = self.request.POST.get("password1")
        user = authenticate(email=email, password=password)
        if user is not None:
            login(self.request, user)
            return redirect("/accounts/edit-profile/%i" % (user.id - 1))

    def form_invalid(self, form):
        messages.add_message(
            self.request, messages.ERROR, "Invalid email or password"
        )
        return super().form_invalid(form)



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

    
class ChangePasswordDoneView(TemplateView):
    template_name = "registration/changepassword_done.html"







class PasswordResetView(FormView):
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
    


    


class ResetPasswordDoneView(TemplateView):
    template_name = "registration/resetpassword_done.html"


# def ResetView(req, token):
#     if req.method == "Get":
#         return render(req, "registration/resetpassword_confirm.html")

#     elif req.method == "Post":
#         form = ResetForm(req.POST)
#         token = req.POST.get("token")
#         user_data = AccessToken(token)
#         user_id = user_data["user_id"]
#         user = get_object_or_404(CustomeUser, id=user_id)
#         if form.is_valid():
#             pass1 = form.cleaned_data["password1"]
#             user.set_password(pass1)
#             user.save()
#             return redirect("acoounts:reset_done")

#     # def post(self, request, *args, **kwargs):
#     #     user_data = AccessToken(kwargs.get("token"))
#     #     user_id = user_data["user_id"]
#     #     user = get_object_or_404(CustomeUser, id=user_id)
#     #     password = kwargs.get('password')


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
        return super().form_valid(form)
    
   



class ResetDoneView(TemplateView):
    template_name = "registration/resetpassword_complete.html"
