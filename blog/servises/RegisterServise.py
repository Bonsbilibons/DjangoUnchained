from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.views import View
from blog.forms import UserCreationForm
from blog.models import User
from django.core.mail import send_mail
import uuid

class Register(View):
    template_name = 'registration/register.html' 
    def get(self , request):
        context = {
             'form' : UserCreationForm()
             }
        return render(request , self.template_name , context)

    def post(self , request ):
        form = UserCreationForm(request.POST)
    
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username = username , password = password )
            user_is_valid = User.objects.get(username = form.cleaned_data.get('username'))
            user_is_valid.is_active = 0
            user_is_valid.unique_id = str(uuid.uuid4())
            user_is_valid.save()
            send_mail(
            'Confirm',
            f'Click on this url to verify your email http://127.0.0.1:8000/blog/confirmation-of-email-for-registration/{user_is_valid.unique_id}',
            'ivanbazelian@gmail.com',
            [form.cleaned_data.get('email')],
            fail_silently=False
            )
            return redirect('/blog/redirect-to-mail-to-confirm-email/')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)