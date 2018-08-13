# candidates views.py

from django.shortcuts import render
from django.views.generic import FormView, DetailView
from django.urls import reverse_lazy

from candidates.forms import CandidateProfileForm
from candidates.models import Candidate_Profile

class CreateCandidateProfileView(FormView):

	template_name = 'candidates/create_candidate_profile.html'
	form_class = CandidateProfileForm

class CandidateProfileView(DetailView):

	model = Candidate_Profile