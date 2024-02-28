from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import (
    AuthenticationForm,
    CustomUserCreation,
    PasswordChangeForm, 
    PasswordResetForm
)
from .models import CustomeUser
from django.views.generic import (
    FormView,
    CreateView,
    TemplateView,
)
# from rest_framework_simplejwt.tokens import RefreshToken
# from rest_framework_simplejwt.tokens import AccessToken
# from mail_templated import EmailMessage
# from .multi_threading import SendEmailWithThreading
from django.contrib.auth.views import PasswordContextMixin
from django.contrib.auth.forms import SetPasswordForm
from django.contrib.auth.tokens import default_token_generator
from django.views.decorators.debug import sensitive_post_parameters
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.core.exceptions import ImproperlyConfigured, ValidationError
from django.http import HttpResponseRedirect
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import REDIRECT_FIELD_NAME, get_user_model
from django.contrib.auth import login as auth_login


UserModel = get_user_model()


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



class ChangePasswordView(FormView):
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






# class ResetPasswordView(FormView):
#     template_name = "registration/resetpassword_form.html"
#     form_class = ResetPasswordForm
#     success_url = "/accounts/ResetPassword/done/"

#     def form_valid(self, form):
#         email = self.request.POST.get("email")
#         user = get_object_or_404(CustomeUser, email=email)
#         if user is not None:
#             token = self.get_tokens_for_user(user)
#             message = EmailMessage(
#                 "registration/resetpassword_email.html",
#                 {"token": token},
#                 "admin@hesam.com",
#                 to=email,
#             )
#             email = SendEmailWithThreading(message)
#             email.start()

#     def get_tokens_for_user(self, user):

#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)

#         # password = self.request.POST.get('password')
#         # user = authenticate(email=email, password=password)
#         # if user is not None:
#         #     login(self.request, user)
#         #     return super().form_valid(form)

class PasswordResetView(PasswordContextMixin,FormView):
    email_template_name = "registration/password_reset_email.html"
    extra_email_context = None
    form_class = PasswordResetForm
    from_email = None
    html_email_template_name = None
    subject_template_name = "registration/password_reset_subject.txt"
    success_url = "/accounts/resetPassword/done/"
    template_name = "registration/resetpassword_form.html"
    title = ("Password reset")
    token_generator = default_token_generator

    # @method_decorator(csrf_protect)
    # def dispatch(self, *args, **kwargs):
    #     return super().dispatch(*args, **kwargs)

    def form_valid(self, form):
        opts = {
            "use_https": self.request.is_secure(),
            "token_generator": self.token_generator,
            "from_email": self.from_email,
            "email_template_name": self.email_template_name,
            "subject_template_name": self.subject_template_name,
            "request": self.request,
            "html_email_template_name": self.html_email_template_name,
            "extra_email_context": self.extra_email_context,
        }
        form.save(**opts)
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

INTERNAL_RESET_SESSION_TOKEN = "_password_reset_token"
class PasswordResetConfirmView(PasswordContextMixin, FormView):
    form_class = SetPasswordForm
    post_reset_login = False
    post_reset_login_backend = None
    reset_url_token = "set-password"
    success_url = "/accounts/reset/done"
    template_name = "registration/resetpassword_confirm.html"
    title = ("Enter new password")
    token_generator = default_token_generator

    @method_decorator(sensitive_post_parameters())
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        if "uidb64" not in kwargs or "token" not in kwargs:
            raise ImproperlyConfigured(
                "The URL path must contain 'uidb64' and 'token' parameters."
            )

        self.validlink = False
        self.user = self.get_user(kwargs["uidb64"])

        if self.user is not None:
            token = kwargs["token"]
            if token == self.reset_url_token:
                session_token = self.request.session.get(INTERNAL_RESET_SESSION_TOKEN)
                if self.token_generator.check_token(self.user, session_token):
                    # If the token is valid, display the password reset form.
                    self.validlink = True
                    return super().dispatch(*args, **kwargs)
            else:
                if self.token_generator.check_token(self.user, token):
                    # Store the token in the session and redirect to the
                    # password reset form at a URL without the token. That
                    # avoids the possibility of leaking the token in the
                    # HTTP Referer header.
                    self.request.session[INTERNAL_RESET_SESSION_TOKEN] = token
                    redirect_url = self.request.path.replace(
                        token, self.reset_url_token
                    )
                    return HttpResponseRedirect(redirect_url)

        # Display the "Password reset unsuccessful" page.
        return self.render_to_response(self.get_context_data())

    def get_user(self, uidb64):
        try:
            # urlsafe_base64_decode() decodes to bytestring
            uid = urlsafe_base64_decode(uidb64).decode()
            user = UserModel._default_manager.get(pk=uid)
        except (
            TypeError,
            ValueError,
            OverflowError,
            UserModel.DoesNotExist,
            ValidationError,
        ):
            user = None
        return user

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs["user"] = self.user
        return kwargs

    def form_valid(self, form):
        user = form.save()
        del self.request.session[INTERNAL_RESET_SESSION_TOKEN]
        if self.post_reset_login:
            auth_login(self.request, user, self.post_reset_login_backend)
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.validlink:
            context["validlink"] = True
        else:
            context.update(
                {
                    "form": None,
                    "title": ("Password reset unsuccessful"),
                    "validlink": False,
                }
            )
        return context



class ResetDoneView(TemplateView):
    template_name = "registration/resetpassword_complete.html"
