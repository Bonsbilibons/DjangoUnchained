from blog.models import User_Info
from blog.models import User
from blog.models import User_Follows
from blog.DTO.User import UpdateUserDataDTO
from blog.functions.functions import handle_uploaded_file

class UserInfoService():
    def get_all_data(self):
        return User_Info.objects.all()

    def get_user_by_id(self, id):
        user = User.objects.get(id=id)
        return user

    def get_data_by_user_id(self, user_id):
        if (User_Info.objects.filter(user=user_id).exists()):
            user_info = User_Info.objects.get(user=user_id)
            user = User.objects.get(id=user_id)
            return user_info

    def get_data_by_username(self, username):
        user = User.objects.get(username=username)
        if(User_Info.objects.filter(user = user.id).exists()):
            user_info = User_Info.objects.get(user = user.id)
            user_array = (
                {
                'id': user.id,
                'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'is_staff': user.is_staff,
                'is_active': user.is_active,
                'date_joined': str(user.date_joined),
                'email': user.email,
                'icon': user.icon,
                'updated_at': str(user.updated_at),
                'biography': user_info.biography,
                'targets': user_info.targets,
                'followers': User_Follows.objects.filter(author=user.id).count()
                }
            )
        else:
            user_array = (
                {
                    'id': user.id,
                    'username': user.username,
                    'first_name': user.first_name,
                    'last_name': user.last_name,
                    'is_staff': user.is_staff,
                    'is_active': user.is_active,
                    'date_joined': str(user.date_joined),
                    'email': user.email,
                    'icon': user.icon,
                    'updated_at': str(user.updated_at),
                    'biography': "",
                    'targets': "",
                    'followers': User_Follows.objects.filter(author=user.id).count()
                }
            )
        return user_array

    def update_data(self, id, dto: UpdateUserDataDTO):
        user = User.objects.get(username = id)
        if dto.icon != '':
            user.icon = handle_uploaded_file(dto.icon, 'user_icon')
        if dto.username != '':
            user.username = dto.username
        if dto.first_name != '':
            user.first_name = dto.first_name
        if dto.last_name != '':
            user.last_name = dto.last_name
        user.updated_at = dto.updated_at
        user.save()

        if(User_Info.objects.filter(user=user.id).exists()):
            user_info = User_Info.objects.get(user=user.id)
            if dto.biography != '':
               user_info.biography = dto.biography
            if dto.targets != '':
               user_info.targets = dto.targets
            user_info.save()
        else:
            user_info = User_Info()
            if dto.biography != '':
                user_info.biography = dto.biography
            if dto.targets != '':
                user_info.targets = dto.targets
            user_info.user = user
            user_info.save()

    def follow(self, author: User(), follower: User()):
        if User_Follows.objects.filter(author=author.id,follower=follower.id):
            follow = User_Follows.objects.get(author=author.id,follower=follower.id)
            follow.delete()
            return False
        else:
            follow = User_Follows()
            follow.author = author
            follow.follower = follower
            follow.save()
            return True

    def is_followed(self, author, follower):
        if User_Follows.objects.filter(author=author, follower=follower).exists():
            return True
        else:
            return False