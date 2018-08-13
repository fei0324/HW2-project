# candidates forms.py

from django import forms
from candidates.models import Candidate_Profile

class CandidateProfileForm(forms.ModelForm):

	class Meta:
		model = Candidate_Profile
		fields = ('resume','biography','LinkedIn','website')