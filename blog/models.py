from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    unique_id = models.CharField("unique_id" , max_length=100)
    class Meta:
        db_table = 'auth_user'