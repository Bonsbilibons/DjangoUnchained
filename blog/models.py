from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    unique_id = models.CharField("unique_id" , max_length=100)
    email = models.EmailField("email", unique=True)
    icon = models.CharField("icon" , max_length=50)
    updated_at = models.DateTimeField("updated_at")
    class Meta:
        db_table = 'auth_user'

class User_Info(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    biography = models.CharField("unique_id" , max_length=2000)
    targets = models.CharField("unique_id" , max_length=200)
    class Meta:
        db_table = 'user_info'