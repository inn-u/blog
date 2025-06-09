from django.contrib import admin

from .models import UserProfile

# admin.site.register(User)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'nickname', 'first_name', 'last_name')
    search_fields = ('nickname', 'user__email', 'first_name', 'last_name')
