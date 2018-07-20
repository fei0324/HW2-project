from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView
from django.urls import reverse, reverse_lazy
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
#from django.contrib.auth.views import LoginView

from all_users.forms import UserSignUpForm, CustomLoginForm

class SignUp(CreateView):
	form_class = UserSignUpForm
	success_url = reverse_lazy('login')
	template_name = 'all_users/signup.html'

def CustomLoginView(request):
	form = CustomLoginForm(request.POST or None)
	if request.method == 'POST' and form.is_valid():
		user = form.login(request)
		if user:
			if user.is_candidate:
				login(request, user)
				print("user is logged in.")
				return HttpResponseRedirect(reverse('test_candidate'))
			elif user.is_employer:
				login(request, user)
				print("user is logged in.")
				return HttpResponseRedirect(reverse('test_employer'))
	return render(request, 'all_users/login.html', {'login_form': form})

class TestCandidatePage(TemplateView):
	template_name = 'all_users/test_candidate.html'

class TestEmployerPage(TemplateView):
	template_name = 'all_users/test_employer.html'