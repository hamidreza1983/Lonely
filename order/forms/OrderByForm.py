from django import forms
from ..models import OrderBy

class OrderByForm(forms.ModelForm):

    class Meta:
        model = OrderBy
        fields = ['first_name', 'last_name', 'email', 'phone']