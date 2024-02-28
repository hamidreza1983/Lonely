from django import forms


class ResetpasswordConfirm(forms.Form):

    new_password1 = forms.CharField(
        label=("New password"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new_password1"}),
    )

    new_password2 = forms.CharField(
        label=("New password confirmation"),
        strip=False,
        widget=forms.PasswordInput(attrs={"autocomplete": "new_password2"}),
    )
