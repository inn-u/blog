from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView

from .forms import CustomUserChangeForm, CustomUserCreationForm
from .models import UserProfile
from blog.models import Post


class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'user-dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user'] = user
        context['profile'] = getattr(user, 'profile', None)
        context['title'] = 'Dashboard'
        context['user_posts'] = Post.objects.filter(author=user)
        return context


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'user-register.html', {'form': form})


class UserProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'user-profile-update.html'
    model = UserProfile
    form_class = CustomUserChangeForm
    success_url = reverse_lazy('dashboard')

    def get_object(self, queryset=None):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile
