from django import forms

from .models import User

class StudentRegistration(forms.ModelForm):
	class Meta:
		model = User
		fields =['userid','name','email','phone']
		widgets = {
		'userid': forms.TextInput(attrs={'class':'form-control'}),
		'name': forms.TextInput(attrs={'class':'form-control'}),
		'email': forms.EmailInput(attrs={'class':'form-control'}),
		'phone': forms.TextInput(attrs={'class':'form-control'}),
		}
