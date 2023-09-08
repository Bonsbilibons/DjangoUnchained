from django.shortcuts import render
from .servises.Confirmation_of_email import confirmation

def main_page(request):
    return render(request, 'blog/front_page.html')

def redirect_to_mail_to_confirm_email(request):
    return render(request, 'registration/redirect_to_mail.html')

def confirmation_of_email_for_registration(request, id):
    confirmation(request, id)
    return render(request, 'registration/confirmation_of_email.html')