from django import forms


class  ContactsForm(forms.Form):
	name = forms.CharField(max_length=30)
	email = forms.EmailField()
	message = forms.CharField(widget=forms.Textarea)