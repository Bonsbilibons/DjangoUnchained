from blog.models import User_Info
from blog.models import User
from blog.DTO.User import UpdateUserDataDTO
from blog.functions.functions import handle_uploaded_file

class UserInfoService():
    def get_all_data(self):
        return User_Info.objects.all()

    def get_data_by_username(self, user_id):
        user_info = User_Info.objects.get(user = user_id)
        return user_info

    def update_data(self, id, dto: UpdateUserDataDTO):
        user = User.objects.get(username = id)
        user_info = User_Info.objects.get(user = user.id)
        if dto.icon != '':
            user.icon = handle_uploaded_file(dto.icon)
        if dto.username != '':
            user.username = dto.username
        if dto.first_name != '':
            user.first_name = dto.first_name
        if dto.last_name != '':
            user.last_name = dto.last_name
        user.updated_at = dto.updated_at
        user.save()
        if dto.biography != '':
           user_info.biography = dto.biography
        if dto.targets != '':
           user_info.targets = dto.targets
        user_info.save()
