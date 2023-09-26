from blog.models import User
from blog.models import Posts
from blog.models import Posts_Images

from blog.DTO.Posts import CreatePostDTO

from blog.functions.functions import save_uploaded_files

from django.conf import settings

import json



class PostService():
    def get_posts_by_user_id(self, user_id):
        posts = Posts.objects.filter(user = user_id)
        return posts

    def get_posts_by_username(self, username):
        user = User.objects.get(username=username)
        posts = Posts.objects.filter(user = user.id)
        posts_with_images = []
        for post in posts:
            posts_with_images.append(
                {
                    'id': post.id,
                    'title': post.title,
                    'description': post.description,
                    'updated_at': post.updated_at,
                    'created_at': post.created_at,
                    'user': post.user,
                    'images': Posts_Images.objects.filter(post = post.id)
                }
            )
        return posts_with_images

    def create_post(self, dto: CreatePostDTO):
        user = User.objects.get(username=dto.user)
        post = Posts()
        post.title = dto.title
        post.description = dto.description
        post.user = user
        post.updated_at = dto.updated_at
        post.created_at = dto.created_at
        post.save()
        save_uploaded_files(dto.images, post)