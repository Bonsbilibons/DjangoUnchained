from django.shortcuts import render,redirect
from django.http import JsonResponse
import http.client, urllib.parse

from .servises.Confirmation_of_email import confirmation
from .servises.UserInfoService import UserInfoService
from .servises.PostsService import PostService
from .servises.SearchService import SearchService

from .DTO.User.UpdateUserDataDTO import UpdateUserDataDTO
from .DTO.Posts.CreatePostDTO import CreatePostDTO

import json


def main_page(request):
    return render(request, 'blog/front_page.html')

def redirect_to_mail_to_confirm_email(request):
    return render(request, 'registration/redirect_to_mail.html')

def confirmation_of_email_for_registration(request, id):
    confirmation(request, id)
    return render(request, 'registration/confirmation_of_email.html')

def user_information(request, id):
    user = UserInfoService()
    posts = PostService()
    return render(request, 'blog/user-information.html', {'id': id, 'user_data': user.get_data_by_username(id), 'posts': reversed(posts.get_posts_by_username(id))})

def user_information_update(request, id):
    user = UserInfoService()
    return render(request, 'blog/user-data-update.html', {'user_data': user.get_data_by_username(id)})

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
    return redirect('/blog/user-information/'+ id)

def create_post(request, id):
    post = PostService()
    create_post_dto = CreatePostDTO(
        request.POST['title'],
        request.POST['description'],
        request.FILES.getlist('images'),
        id
    )
    post.create_post(create_post_dto)
    return redirect('/blog/user-information/'+ id)

def like_post(request):
    post_service = PostService()
    user_info_service = UserInfoService()

    is_liked = post_service.like_post(
        user_info_service.get_user_by_id(request.user.id),
        post_service.get_post_by_post_id(request.POST['post_id'])
    )

    if int(request.user.id) != int(request.POST['data_user_id']):
        conn = http.client.HTTPConnection('127.0.0.1:3003')
        params = {
            'user_id': request.user.id,
            'username': request.user.username,
            'post_id': request.POST['post_id'],
            'data_user_id': request.POST['data_user_id'],
            'is_liked': is_liked
        }
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        conn.request('POST', '/like_post', json.dumps(params), headers)
    return JsonResponse({
        'status': is_liked
    })

def is_post_liked(request):
    is_liked = PostService()
    status = is_liked.is_post_liked(request.POST['post_id'], request.user.id)
    return JsonResponse({
        'status': status
    })

def main_search(request):
    search_request = request.POST['search']
    result = SearchService()
    return render(request, 'blog/main-search.html', {'results': result.search_by_username(search_request)})

def follow_on_user(request):
    follow = UserInfoService()
    author = UserInfoService()
    follower = UserInfoService()

    status = follow.follow(author.get_user_by_id(request.POST['author_id']), follower.get_user_by_id(request.user.id))

    if int(request.POST['author_id']) != int(request.user.id):
        conn = http.client.HTTPConnection('127.0.0.1:3003')
        params = {
            'author_id': request.POST['author_id'],
            'follower': request.user.username,
            'follower_id': request.user.id,
            'is_followed': status
        }
        headers = {"Accept": "application/json", "Content-Type": "application/json"}
        conn.request('POST', '/follow_on_user', json.dumps(params), headers)

    return JsonResponse({
        'status': status
    })

def is_followed_on(request):
    is_followed = UserInfoService()
    status = is_followed.is_followed(
        request.POST['author_id'],
        request.POST['follower_id']
    )
    return JsonResponse({
        'status': status
    })