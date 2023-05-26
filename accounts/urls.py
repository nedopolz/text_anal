from django.urls import path

from .views import (LogInView, SignUpView, ActivateView, LogOutView, ChangeProfileView, )

app_name = 'accounts'

urlpatterns = [
    path('log-in/', LogInView.as_view(), name='log_in'),
    path('log-out/', LogOutView.as_view(), name='log_out'),

    path('sign-up/', SignUpView.as_view(), name='sign_up'),
    path('activate/<code>/', ActivateView.as_view(), name='activate'),

    path('change/profile/', ChangeProfileView.as_view(), name='change_profile'),
]
