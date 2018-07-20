# candidates models.py

from django.db import models
from all_users.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

class Candidate_Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	resume = models.FileField(upload_to='resumes/')
	biography = models.TextField()
	LinkedIn = models.URLField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.user.username

# Everytime a user signs up and choses user type candidate
# it automatically creats a candidate profile
def save_signal(sender, instance, created, **kwargs):
	if created and is_candidate:
		instance.save()

models.signals.pre_save.connect(save_signal, Candidate_Profile)
