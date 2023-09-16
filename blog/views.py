from django.shortcuts import render,redirect

from .servises.Confirmation_of_email import confirmation
from .servises.UserInfoService import UserInfoService

from .DTO.User.UpdateUserDataDTO import UpdateUserDataDTO

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

def user_information_save(request, id):
    user = UserInfoService()
    update_user_data_dto = UpdateUserDataDTO(
        request.FILES['icon'] if len(request.FILES) > 0 and request.FILES['icon'] else '',
        request.POST['username'],
        request.POST['first_name'],
        request.POST['last_name'],
        request.POST['biography'],
        request.POST['targets'],
    )
    user.update_data(id, update_user_data_dto)
    return redirect('/blog/main')