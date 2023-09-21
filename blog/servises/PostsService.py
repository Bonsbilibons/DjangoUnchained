from blog.models import User
from blog.models import Posts
from blog.DTO.Posts import CreatePostDTO
from blog.functions.functions import handle_uploaded_files

class PostService():
    def create_post(self, dto: CreatePostDTO):
        user = User.objects.get(username=dto.user)
        post = Posts()
        post.title = dto.title
        post.description = dto.description
        post.images = handle_uploaded_files(dto.images)
        post.user = user
        post.updated_at = dto.updated_at
        post.created_at = dto.created_at
        post.save()
