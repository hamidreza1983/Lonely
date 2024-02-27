from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import (
    AuthenticationForm,
    ResetPasswordForm,
    ResetForm,
    ChangePasswordForm,
    CustomUserCreation,
)
from .models import CustomeUser
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
)
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from mail_templated import EmailMessage
from .multi_threading import SendEmailWithThreading
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



def ChangePasswordView(req):
    if req.metod == "GET":
        return render(req, "registration/changepassword_form.html")
    elif req.method == "POST":
        form = ChangePasswordForm(req.POST)

        if form.is_valid():
            form.check_old_password(req)
            form.set_new_password(req)
            return redirect("accounts:hange_password_done")


class ChangePasswordDoneView(TemplateView):
    template_name = "registration/changepassword_done.html"


class ResetPasswordView(FormView):
    template_name = "registration/resetpassword_form.html"
    form_class = ResetPasswordForm
    success_url = "/accounts/ResetPassword/done/"

    def form_valid(self, form):
        email = self.request.POST.get("email")
        user = get_object_or_404(CustomeUser, email=email)
        if user is not None:
            token = self.get_tokens_for_user(user)
            message = EmailMessage(
                "registration/resetpassword_email.html",
                {"token": token},
                "admin@hesam.com",
                to=email,
            )
            email = SendEmailWithThreading(message)
            email.start()

    def get_tokens_for_user(self, user):

        refresh = RefreshToken.for_user(user)
        return str(refresh.access_token)

        # password = self.request.POST.get('password')
        # user = authenticate(email=email, password=password)
        # if user is not None:
        #     login(self.request, user)
        #     return super().form_valid(form)


class ResetPasswordDoneView(TemplateView):
    template_name = "registration/resetpassword_done.html"


def ResetView(req, token):
    if req.method == "Get":
        return render(req, "registration/resetpassword_confirm.html")

    elif req.method == "Post":
        form = ResetForm(req.POST)
        token = req.POST.get("token")
        user_data = AccessToken(token)
        user_id = user_data["user_id"]
        user = get_object_or_404(CustomeUser, id=user_id)
        if form.is_valid():
            pass1 = form.cleaned_data["password1"]
            user.set_password(pass1)
            user.save()
            return redirect("acoounts:reset_done")

    # def post(self, request, *args, **kwargs):
    #     user_data = AccessToken(kwargs.get("token"))
    #     user_id = user_data["user_id"]
    #     user = get_object_or_404(CustomeUser, id=user_id)
    #     password = kwargs.get('password')


class ResetDoneView(TemplateView):
    template_name = "registration/resetpassword_complete.html"
