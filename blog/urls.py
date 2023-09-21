from django.contrib import admin
from django.urls import path, include
from . import views
from .servises.RegisterServise import Register
from . servises.LoginServise import Login

urlpatterns = [
    path('main/', views.main_page, name='main_page'),
    path('registration/', Register.as_view(), name='register' ),
    path('login/', Login.as_view(), name='login' ),
    path('account/' , include('django.contrib.auth.urls')),
    path('redirect-to-mail-to-confirm-email/', views.redirect_to_mail_to_confirm_email, name='redirect_to_mail_to_confirm_email'),
    path('confirmation-of-email-for-registration/<id>', views.confirmation_of_email_for_registration, name='confirmation_of_email_for_registration'),
    path('user-information/<id>', views.user_information, name='user-information'),
    path('user-information/<id>/update', views.user_information_update, name='user-information-update'),
    path('user-information/<id>/update/save', views.user_information_save, name='user-information-save'),
    path('user-information/<id>/create-post', views.create_post, name='create_post')
]