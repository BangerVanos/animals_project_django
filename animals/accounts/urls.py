from django.urls import path
from . import views
from django.contrib.auth.views import login_required


app_name = 'accounts'

urlpatterns = [
    path('profile/', login_required(views.ProfileView.as_view()), name='profile'),
    path('profile/change/', login_required(views.ProfileChangeView.as_view()), name='profile_change'),
    path('register/', views.UserRegistrationView.as_view(), name='register'),
]
