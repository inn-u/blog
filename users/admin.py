# from django.contrib import admin
#
# from .forms import UserChangeForm, UserCreationForm
# from .models import Client, User
#
#
# @admin.register(User)
# class UserAdmin(admin.ModelAdmin):
#     form = UserChangeForm
#     add_form = UserCreationForm
#
#     list_display = ("email", "is_active", "is_staff", "is_superuser", "is_blocked")
#     list_filter = ("is_active", "is_staff", "is_superuser", "is_blocked")
#     short_fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         ("Important dates", {"fields": ("last_login",)}),
#     )
#     fieldsets = (
#         (None, {"fields": ("email", "password")}),
#         (
#             "Permissions",
#             {"fields": ("is_active", "is_staff", "is_superuser", "is_blocked")},
#         ),
#         ("Relations", {"fields": ("groups", "user_permissions")}),
#         ("Important dates", {"fields": ("last_login",)}),
#     )
#     search_fields = ("email",)
#     ordering = ("email",)
#     readonly_fields = ("email", "last_login")
#
#
# @admin.register(Client)
# class ClientAdmin(admin.ModelAdmin):
#     list_display = ("id", "email")
#     search_fields = ("email", "first_name", "last_name")
