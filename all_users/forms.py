# all_users forms.py

from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth import authenticate

from all_users.models import User

class UserSignUpForm(UserCreationForm):

	class Meta():
		model = User
		fields = ('username', 'email', 'user_type', 'password1', 'password2')

class CustomLoginForm(forms.ModelForm):

	password = forms.CharField(widget=forms.PasswordInput())

	class Meta:
		model = User
		fields = ('username', 'password')

	def clean(self):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		if not user or not user.is_active:
			raise forms.ValidationError("Sorry, the login was invalid. Please try again!")

		return self.cleaned_data

	def login(self, request):
		username = self.cleaned_data.get('username')
		password = self.cleaned_data.get('password')
		user = authenticate(username=username, password=password)
		return user