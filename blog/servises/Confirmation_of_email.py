from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import View
from blog.forms import UserCreationForm
from blog.models import User
from django.core.mail import send_mail

def confirmation(request, id):
	user = User.objects.get(unique_id = id)
	user.is_active = 1
	user.save()
	login(request , user)
	send_mail(
            'Confirm',
            f'My congratulations! Yours email is verified',
            'ivanbazelian@gmail.com',
            [user.email],
            fail_silently=False
    )