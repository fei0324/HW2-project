# candidates models.py

from django.db import models
from django.urls import reverse
from django.db.models.signals import post_save
#from django.dispatch import receiver

from all_users.models import User

class Candidate_Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	resume = models.FileField(upload_to='resumes/')
	biography = models.TextField()
	LinkedIn = models.URLField(blank=True)
	website = models.URLField(blank=True)

	def __str__(self):
		return self.user.username

	# Need to edit this save method
	# self.user should be the user with the same username
	def save(self):
		pass 

	def get_absolute_url(self):
		return reverse('candidates:profile-detail')


# Everytime a user signs up and choses user type candidate
# it automatically creats a candidate profile
def create_candidate_profile(sender, instance, created, **kwargs):

	if created and instance.is_candidate:
		print("Creating candidate profile")
		Candidate_Profile.objects.create(user=instance)
		print("Candidate profile created.")

post_save.connect(create_candidate_profile, sender=User)

def save_candidate_profile(sender, instance, **kwargs):
	print("Saving candidate profile.")
	instance.candidate_profile.save()
	print("Candidate profile saved.")

post_save.connect(save_candidate_profile, sender=User)
