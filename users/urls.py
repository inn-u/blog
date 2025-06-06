from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.urls import path, reverse_lazy

from .views import DashboardView, UserProfileUpdateView, register

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path(
        'dashboard/',
        DashboardView.as_view(template_name='user-dashboard.html'),
        name='dashboard',
    ),
    path(
        'logout/',
        auth_views.LogoutView.as_view(next_page=reverse_lazy('login')),
        name='logout',
    ),
    path('register/', register, name='register'),
    path(
        'edit-profile/',
        UserProfileUpdateView.as_view(template_name='user-profile-update.html'),
        name='edit-profile',
    ),
]
