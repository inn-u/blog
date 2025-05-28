# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.db import models
#
# from utils.model_behaviour import Timestampable
#
# from .manager import UserManager
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True)
#     is_active = models.BooleanField(
#         default=True, verbose_name='Active',
#         help_text='Is user active or not'
#     )
#     is_staff = models.BooleanField(
#         default=False, verbose_name='Staff status',
#         help_text='Is user staff of client'
#     )
#     is_blocked = models.BooleanField(
#         default=False, verbose_name='Blocked',
#         help_text='Is user blocked'
#     )
#
#     objects = UserManager()
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     class Meta:
#         verbose_name = 'user'
#         verbose_name_plural = 'users'
#
#
# class Client(Timestampable):
#     user = models.OneToOneField(
#         User, related_name='client', on_delete=models.CASCADE
#     )
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=100)
#     date_of_birth = models.DateField(
#         verbose_name='Date of Birth', null=True, blank=True
#     )
#
#     def __str__(self):
#         return f'user_id={self.user.id} email={self.user.email}'
#
#     @property
#     def email(self) -> str:
#         return self.user.email
