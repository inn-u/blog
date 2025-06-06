from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'nickname', 'avatar']
