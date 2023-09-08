from django.contrib import admin
from django.urls import path, include
from . import views
from .servises.RegisterServise import Register

urlpatterns = [
    path('main/', views.main_page, name='main_page'),
    path('registration/', Register.as_view(), name='register' ),
    path('account/' , include('django.contrib.auth.urls')),
    path('redirect-to-mail-to-confirm-email/', views.redirect_to_mail_to_confirm_email, name='redirect_to_mail_to_confirm_email'),
    path('confirmation-of-email-for-registration/<id>', views.confirmation_of_email_for_registration, name='confirmation_of_email_for_registration')
]