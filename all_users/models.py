# all_users models.py

from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

	candidate = 'candidate'
	employer = 'employer'

	user_type_choices = (
		(candidate, 'Candidate'),
		(employer, 'Employer'),
		)

	user_type = models.CharField(
		max_length = 50,
		choices = user_type_choices,
		default = candidate
		)

	#is_candidate = models.BooleanField(default=False)
	#is_employer = models.BooleanField(default=False)

	@property
	def is_candidate(self):
		if self.user_type == 'candidate':
			print(self.username)
			print("user_type is candidate")
			return True
		return False

	@property
	def is_employer(self):
		if self.user_type == 'employer':
			print(self.username)
			print("user_type is employer")
			return True
		return False