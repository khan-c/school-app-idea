from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'first_name', 'last_name', 'role']
    list_filter = ('email', 'first_name', 'last_name', 'role')
    fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name')}),
        ('Other Info', {'fields': ('age', 'birthdate', 'profile_pic')}),
        ('Teachers', {'fields': ('teachers',)}),
        ('Parents', {'fields': ('parents',)}),
        ('Permissions', {'fields': ('role', 'is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password',
                       'password2', 'first_name', 'last_name', 'role')}),
        ('Other Info', {'fields': ('age', 'birthdate', 'profile_pic')}),
        ('Teachers', {'fields': ('teachers',)}),
        ('Parents', {'fields': ('parents',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
