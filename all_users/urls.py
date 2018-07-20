# all_users urls.py

from django.urls import path
from django.contrib.auth import views as auth_views

from all_users import views


app_name = 'all_users'

urlpatterns = [
	path('signup/', views.SignUp.as_view(), name='signup'),
	#path('login/', auth_views.LoginView.as_view(template_name='all_users/login.html'), name='login'),
	path('login/', views.CustomLoginView, name='login'),
	path('test_candidate/', views.TestCandidatePage.as_view(), name='test_candidate'),
	path('test_employer/', views.TestEmployerPage.as_view(), name='test_employer'),
]