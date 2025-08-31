from django.urls import path
from .views import RegisterView, LoginView, ProfileView, LogoutView, ProfileUpdateView

app_name = 'users'

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register_page'),
    path('login/', LoginView.as_view(), name='login_page'),
    path('logout/', LogoutView.as_view(), name='logout_page'),
    path("profile/", ProfileView.as_view(), name='profile_page'),
    path('profile/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
]
