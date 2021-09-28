from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin

from backend.core.models import User, Upload


@admin.register(User)
class UserAdmin(AuthUserAdmin):
    fieldsets = None


admin.site.register(Upload)
