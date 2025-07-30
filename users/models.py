from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.templatetags.static import static

from .user_manager import UserManager


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, verbose_name='email')
    name = models.CharField(max_length=150, blank=True, verbose_name='Name')
    role = models.CharField(max_length=10, default='user', verbose_name='Role')

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    date_of_birth = models.DateField(
        verbose_name='Date of Birth', null=True, blank=True
    )

    nickname = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    about_me = models.CharField(
        max_length=240, blank=True, null=True, verbose_name='About author'
    )

    @property
    def email(self) -> str:
        return self.user.email

    def __str__(self):
        return f'user_id={self.id} email={self.email}'

    def get_avatar_url(self):
        if self.avatar:
            return self.avatar.url
        return static('placeholders/avatar-placeholder.png')
