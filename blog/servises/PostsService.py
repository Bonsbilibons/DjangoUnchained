from blog.models import User
from blog.models import Posts
from blog.models import Posts_Images
from blog.models import Posts_Likes

from blog.DTO.Posts import CreatePostDTO

from blog.functions.functions import save_uploaded_files

from django.conf import settings

import json



class PostService():
    def get_posts_by_user_id(self, user_id):
        user = User.objects.get(id=user_id)
        posts = Posts.objects.filter(user=user.id)
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
                    'images': Posts_Images.objects.filter(post=post.id)
                }
            )
        return posts_with_images

    def get_posts_by_username(self, username):
        user = User.objects.get(username=username)
        posts = Posts.objects.filter(user=user.id)
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
                    'images': Posts_Images.objects.filter(post = post.id),
                    'likes': len(Posts_Likes.objects.filter(post=post.id))
                }
            )
        return posts_with_images

    def get_post_by_post_id(self, id):
        post = Posts.objects.get(id=id)
        return post

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

    def like_post(self, user: User(), post: Posts()):
        if(Posts_Likes.objects.filter(user=user.id, post=post.id).exists()):
            like = Posts_Likes.objects.get(user=user.id, post=post.id)
            like.delete()
        else:
            like = Posts_Likes()
            like.user = user
            like.post = post
            like.save()