from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomeUser, Profile
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions
from rest_framework.authtoken.models import Token

class CustomUserCreation(UserCreationForm):

    class Meta:
        model = CustomeUser
        fields = [ 'email','username', 'password1', 'password2']


class AuthenticationForm(forms.Form):
    """
    Base class for authenticating users. Extend this to get a form that accepts
    username/password logins.
    """

    email = forms.EmailField()
    password = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )


class EditProfile(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [ 'user','first_name', 'last_name', 'image', 'phone', 'address']



class ResetPasswordForm(forms.ModelForm): 
    email = forms.EmailField()


class ResetForm(forms.ModelForm):
    password1 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    password2 = forms.CharField(
        label=("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "current-password"}),
    )
    def is_valid(self) -> bool:
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if password1 != password2:
            raise forms.ValidationError({"detail": "password dose not confirmed"})

        try:

            validate_password(password1)

        except exceptions.ValidationError as e:

            raise forms.ValidationError({"detail": list(e.messages)})

        return super().is_valid()
    



class ChangePasswordForm(forms.ModelForm):
    old_password = forms.CharField(max_length=20)
    new_password1 = forms.CharField(max_length=20)
    new_password2 = forms.CharField(max_length=20)

    def validate(self, attrs):
        pass1 = self.cleaned_data("new_password1")
        pass2 = self.cleaned_data("new_password2")

        if pass1 != pass2:
            raise forms.ValidationError(
                {"detail": "pass1 and pass2 must be the same"}
            )

        return super().is_validate()

    def check_old_password(self, request):

        old_pass = self.cleaned_data("old_password")
        pass1 = self.cleaned_data("new_password1")
        user = request.user
        if not user.check_password(old_pass):
            raise forms.ValidationError(
                {"detail": "old_password is not confirmed"}
            )

        if old_pass == pass1:
            raise forms.ValidationError(
                {"detail": "old_password can not same as new pass"}
            )

        return self.cleaned_data

    def set_new_password(self, request):
        pass1 = self.cleaned_data("new_password1")
        user = request.user
        try:

            validate_password(pass1)

        except exceptions.ValidationError as e:

            raise forms.ValidationError({"detail": list(e.messages)})

        user.set_password(pass1)
        user.save()
        return self.cleaned_data

    def create_new_token(self, request):
        user = request.user

        try:
            user.auth_token.delete()
            Token.objects.create(user=user)
        except:
            Token.objects.create(user=user)
        token = Token.objects.get(user=user)
        return token
