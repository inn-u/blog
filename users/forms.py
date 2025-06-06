from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from .models import User, UserProfile


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['first_name', 'last_name', 'date_of_birth', 'nickname', 'avatar']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
        }
