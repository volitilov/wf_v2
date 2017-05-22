from django.forms import ModelForm
from models import Mesage



class MesageForm(ModelForm):
	class Meta:
		model = Mesage
		