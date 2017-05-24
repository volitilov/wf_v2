from django import forms
from .models import Mesage


class ContactsForm(forms.ModelForm):
    class Meta:
        model = Mesage
        fields = "__all__"
    