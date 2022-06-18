from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from accounts.models import User


class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets


admin.site.register(User, CustomUserAdmin)
