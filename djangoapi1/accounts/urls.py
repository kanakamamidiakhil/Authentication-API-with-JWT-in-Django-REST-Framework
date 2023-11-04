from django.urls import path
from accounts.views import UserRegistrationView
from accounts.views import UserLoginView
from accounts.views import UserProfileView
from accounts.views import UserChangePasswordView
from accounts.views import SendPasswordResetEmailView
from accounts.views import UserPasswordResetView

urlpatterns = [
    path('register/',UserRegistrationView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('profile/',UserProfileView.as_view(),name='profile'),
    path('changepassword/',UserChangePasswordView.as_view(),name='changepassword'),
    path('send-reset-password-email/',SendPasswordResetEmailView.as_view(),name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/',UserPasswordResetView.as_view(),name='reset-password'),
]
