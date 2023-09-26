from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    unique_id = models.CharField("unique_id", max_length=100)
    email = models.EmailField("email", unique=True)
    icon = models.CharField("icon", max_length=50)
    updated_at = models.DateTimeField("updated_at")
    class Meta:
        db_table = 'auth_user'

class User_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biography = models.CharField("unique_id", max_length=2000)
    targets = models.CharField("unique_id", max_length=200)
    class Meta:
        db_table = 'user_info'

class Posts(models.Model):
    title = models.CharField("title", max_length=100)
    description = models.CharField("description", max_length=2000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField("updated_at")
    created_at = models.DateTimeField("created_at")
    class Meta:
        db_table = 'posts'

class Posts_Images(models.Model):
    name = models.CharField("title", max_length=100)
    post = models.ForeignKey(Posts, on_delete=models.CASCADE)
    class Meta:
        db_table = 'Posts_Images'