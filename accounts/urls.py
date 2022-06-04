from django.urls import path
from django.contrib.auth.views import (
PasswordResetView,
PasswordResetConfirmView,
PasswordResetDoneView,
PasswordResetConfirmView,
PasswordResetCompleteView,
PasswordChangeView,
PasswordChangeDoneView,
)
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('fetch', views.fetch, name='fetch'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('reset_password/', PasswordResetView.as_view(template_name="accounts/password_reset.html"), name="reset_password"),
    path('reset_password_sent/', PasswordResetDoneView.as_view(template_name="accounts/password_reset_senr.html"),name="password_reset_done"),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path('reset_password_complete/', PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"),name="password_reset_complete"),
    ]
