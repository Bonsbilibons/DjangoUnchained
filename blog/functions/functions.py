import uuid
import os
from django.conf import settings

from blog.models import Posts
from blog.models import Posts_Images

def save_uploaded_files(posts_images, post):
    media_root = os.path.join(settings.MEDIA_ROOT, "posts")
    folder_path = os.path.join(media_root, str(post.id))
    os.makedirs(folder_path)
    for image in posts_images:
        post_image = Posts_Images()
        post_image.post = post
        post_image.name = image
        post_image.save()
        with open(os.path.join(folder_path, image.name), 'wb+') as destination:
            for chunk in image.chunks():
                destination.write(chunk)

def handle_uploaded_file(f):
    _, extension = os.path.splitext(f.name)
    name = str(uuid.uuid4()) + extension
    with open(settings.MEDIA_ROOT + "posts/" + name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return name

def handle_uploaded_files(array):
    ready_array = []
    for i in array:
        _, extension = os.path.splitext(i.name)
        name = str(uuid.uuid4()) + extension
        with open(settings.MEDIA_ROOT + name, 'wb+') as destination:
            for chunk in i.chunks():
                destination.write(chunk)
        ready_array.append(name)
    return ready_array