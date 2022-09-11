from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from .models import Account


class CustomUserAdmin(UserAdmin):
    model = Account
    list_display = ["code", "name", "is_staff"]
    search_fields = ("name", )
    fieldsets = (
        (None, {"fields": ("code", "password")}),
    )
    ordering = ('code',)


admin.site.register(Account, CustomUserAdmin)
