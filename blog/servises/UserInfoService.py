from blog.models import User_Info

class UserInfoService():
    def get_all_data(self):
        return User_Info.objects.all()

    def get_data_by_username(self, user_id):
        user_info = User_Info.objects.get(user = user_id)
        return user_info