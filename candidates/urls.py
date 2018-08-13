from django.urls import path

from candidates import views

app_name = 'candidates'

urlpatterns = [
	path('create/<username>', views.CreateCandidateProfileView.as_view(), name='create'),
	path('profile/<pk:user.pk>', views.CandidateProfileView.as_view(), name='profile-detail'),

]