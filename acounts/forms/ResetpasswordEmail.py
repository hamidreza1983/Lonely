from django import forms


class ResetpasswordEmail(forms.Form):
    email = forms.EmailField(
        label=("Email"),
        max_length=254,
        widget=forms.EmailInput(attrs={"autocomplete": "email"}),
    )
