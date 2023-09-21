import uuid
import os
from django.conf import settings


def handle_uploaded_file(f):
    _, extension = os.path.splitext(f.name)
    name = str(uuid.uuid4()) + extension
    with open(settings.MEDIA_ROOT + name, 'wb+') as destination:
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