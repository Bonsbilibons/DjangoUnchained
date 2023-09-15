from django.shortcuts import render,redirect
from .servises.Confirmation_of_email import confirmation
from .servises.UserInfoService import UserInfoService

def main_page(request):
    return render(request, 'blog/front_page.html')

def redirect_to_mail_to_confirm_email(request):
    return render(request, 'registration/redirect_to_mail.html')

def confirmation_of_email_for_registration(request, id):
    confirmation(request, id)
    return render(request, 'registration/confirmation_of_email.html')

def user_information(request, id):
    return render(request, 'blog/user-information.html', {'id': id})

def user_information_update(request, id):
    user = UserInfoService()
    return render(request, 'blog/user-data-update.html', {'user_data': user.get_data_by_username(request.user.id)})