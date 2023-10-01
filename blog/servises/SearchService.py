from blog.models import User_Info
from blog.models import User
from blog.models import Posts
from blog.models import Posts_Images
from blog.models import Posts_Likes

from django.db.models import Q
class SearchService:
    def search_by_username(self, request):
        if request:
            user = User.objects.filter(Q(username__icontains=request) | Q(first_name__icontains=request) | Q(last_name__icontains=request))
            return user
        else:
            return User.objects.all()
