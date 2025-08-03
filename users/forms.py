from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User, UserProfile


class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = (
            'email',
            'password1',
            'password2',
        )

    def save(self, commit=True):
        user = super().save(commit=commit)
        nickname = self.cleaned_data.get('nickname')
        if commit:
            UserProfile.objects.create(user=user, nickname=nickname)
        return user


class CustomUserChangeForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'first_name',
            'last_name',
            'date_of_birth',
            'about_me',
            'nickname',
            'avatar',
        ]
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
            'first_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter first name'}
            ),
            'last_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter last name'}
            ),
            'nickname': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter nickname'}
            ),
            'about_me': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Add few words about you',
                }
            ),
        }
