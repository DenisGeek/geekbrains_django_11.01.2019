from django.db import models
from django.contrib.auth.models import AbstractUser


class ShopUser(AbstractUser):
    # User model
    avatar = models.ImageField(upload_to='users_avatars', blank=True)
    age = models.PositiveIntegerField(verbose_name = 'возраст')