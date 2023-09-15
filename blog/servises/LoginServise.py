from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
from blog.models import User


class Login(View):
    template_name = 'registration/login.html' 
    def get(self, request):
        context = {
             'form' : AuthenticationForm()
             }
        return render(request, self.template_name, context)

    def post(self, request):
        form = AuthenticationForm(request.POST)
        if form.is_valid():
            form.save()
            try:
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username = username , password = password )
            except:
                found_user = User.objects.get(email = form.cleaned_data.get('username'))
                username = found_user.username
                password = form.cleaned_data.get('password')
                user = authenticate(username = username , password = password )
            return redirect('/blog/main')
        context = {
            'form': form
        }
        return render(request, self.template_name, context)