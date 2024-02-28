from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser
# from django.contrib.auth.password_validation import validate_password
# from django.core import exceptions
from django.contrib.auth.forms import _unicode_ci_compare
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.tokens import AccessToken
from mail_templated import EmailMessage
from .multi_threading import SendEmailWithThreading
from django.contrib.auth import password_validation, get_user_model
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.sites.shortcuts import get_current_site
from django.core.exceptions import ValidationError


class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = ["email", "username", "password1", "password2"]


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password"}
        ),
    )



# class ResetPasswordForm(forms.Form):
#     email = forms.EmailField()

#     # class Meta:
#     #     model = CustomeUser
#     #     fields = ["email",]

#     # def is_valid(self) -> bool:
#     #     email = self.cleaned_data['email']
#     #     user = get_object_or_404(CustomeUser, email=email)
#     #     return super().is_valid()

             





# class ResetForm(forms.Form):

#     password1 = forms.CharField(
#         label=("Password"),
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "current-password"}
#         ),
#     )
#     password2 = forms.CharField(
#         label=("Password"),
#         strip=False,
#         widget=forms.PasswordInput(
#             attrs={"autocomplete": "current-password"}
#         ),
#     )


#     # class Meta:
#     #     model = CustomeUser
#     #     fields = ["password1", "password2"]


#     def is_valid(self) -> bool:
#         password1 = self.cleaned_data["password1"]
#         password2 = self.cleaned_data["password2"]

#         if password1 != password2:
#             raise forms.ValidationError(
#                 {"detail": "password dose not confirmed"}
#             )

#         try:

#             validate_password(password1)

#         except exceptions.ValidationError as e:

#             raise forms.ValidationError({"detail": list(e.messages)})

#         return super().is_valid()
    


# class ChangePasswordForm(forms.Form):
#     old_password = forms.CharField(max_length=20)
#     new_password1 = forms.CharField(max_length=20)
#     new_password2 = forms.CharField(max_length=20)


#     def validate(self):
#         pass1 = self.cleaned_data("new_password1")
#         pass2 = self.cleaned_data("new_password2")

#         if pass1 != pass2:
#             raise forms.ValidationError(
#                 {"detail": "pass1 and pass2 must be the same"}
#             )

#         return super().is_validate()

#     def check_old_password(self, request):

#         old_pass = self.cleaned_data("old_password")
#         pass1 = self.cleaned_data("new_password1")
#         user = request.user
#         if not user.check_password(old_pass):
#             raise forms.ValidationError(
#                 {"detail": "old_password is not confirmed"}
#             )

#         if old_pass == pass1:
#             raise forms.ValidationError(
#                 {"detail": "old_password can not same as new pass"}
#             )

#         return self.cleaned_data

#     def set_new_password(self, request):
#         pass1 = self.cleaned_data("new_password1")
#         user = request.user
#         try:

#             validate_password(pass1)

#         except exceptions.ValidationError as e:

#             raise forms.ValidationError({"detail": list(e.messages)})

#         user.set_password(pass1)
#         user.save()
#         return self.cleaned_data

#     def create_new_token(self, request):
#         user = request.user

#         try:
#             user.auth_token.delete()
#             Token.objects.create(user=user)
#         except:
#             Token.objects.create(user=user)
#         token = Token.objects.get(user=user)
#         return token





UserModel = get_user_model()



# class PasswordResetForm(forms.Form):
#     email = forms.EmailField(
#         label=("Email"),
#         max_length=254,
#         widget=forms.EmailInput(attrs={"autocomplete": "email"}),
#     )

#     def get_tokens_for_user(self, user):

#         refresh = RefreshToken.for_user(user)
#         return str(refresh.access_token)

#     # def send_mail(
#     #     self,
#     #     context,
#     #     from_email,
#     #     to_email,
#     #     html_email_template_name=None
        
#     # ):
        




#     def get_users(self, email):
#         """Given an email, return matching user(s) who should receive a reset.

#         This allows subclasses to more easily customize the default policies
#         that prevent inactive users and users with unusable passwords from
#         resetting their password.
#         """
#         email_field_name = UserModel.get_email_field_name()
#         active_users = UserModel._default_manager.filter(
#             **{
#                 "%s__iexact" % email_field_name: email,
#                 "is_active": True,
#             }
#         )
#         return (
#             u
#             for u in active_users
#             if u.has_usable_password()
#             and _unicode_ci_compare(email, getattr(u, email_field_name))
#         )

#     def save(
#         self,
#         domain_override=None,
#         subject_template_name="registration/password_reset_subject.txt",
#         email_template_name="registration/password_reset_email.html",
#         use_https=False,
#         token_generator=default_token_generator,
#         from_email=None,
#         request=None,
#         html_email_template_name=None,
#         extra_email_context=None,
#     ):
#         """
#         Generate a one-use only link for resetting password and send it to the
#         user.
#         """
#         email = self.cleaned_data["email"]
#         if not domain_override:
#             current_site = get_current_site(request)
#             site_name = current_site.name
#             domain = current_site.domain
#         else:
#             site_name = domain = domain_override
#         email_field_name = UserModel.get_email_field_name()
#         for user in self.get_users(email):
#             user_email = getattr(user, email_field_name)
#             context = {
#                 "email": user_email,
#                 "domain": domain,
#                 "site_name": site_name,
#                 "uid": urlsafe_base64_encode(force_bytes(user.pk)),
#                 "user": user,
#                 "token": token_generator.make_token(user),
#                 "protocol": "https" if use_https else "http",
#                 **(extra_email_context or {}),
#             }
#             self.send_mail(
#                 subject_template_name,
#                 email_template_name,
#                 context,
#                 from_email,
#                 user_email,
#                 html_email_template_name=html_email_template_name,
#             )



class SetPasswordForm(forms.Form):
    """
    A form that lets a user set their password without entering the old
    password
    """

    error_messages = {
        "password_mismatch": ("The two password fields didn’t match."),
    }
    new_password1 = forms.CharField(
        label=("New password"),
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
        strip=False,
        help_text=password_validation.password_validators_help_text_html(),
    )
    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new-password"}),
    )

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get("new_password1")
        password2 = self.cleaned_data.get("new_password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError(
                self.error_messages["password_mismatch"],
                code="password_mismatch",
            )
        password_validation.validate_password(password2, self.user)
        return password2

    def save(self, commit=True):
        password = self.cleaned_data["new_password1"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user

class PasswordChangeForm(SetPasswordForm):
    """
    A form that lets a user change their password by entering their old
    password.
    """

    error_messages = {
        **SetPasswordForm.error_messages,
        "password_incorrect": (
            "Your old password was entered incorrectly. Please enter it again."
        ),
    }
    old_password = forms.CharField(
        label=("Old password"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={"autocomplete": "current-password", "autofocus": True}
        ),
    )

    field_order = ["old_password", "new_password1", "new_password2"]

    def clean_old_password(self):
        """
        Validate that the old_password field is correct.
        """
        old_password = self.cleaned_data["old_password"]
        if not self.user.check_password(old_password):
            raise ValidationError(
                self.error_messages["password_incorrect"],
                code="password_incorrect",
            )
        return old_password