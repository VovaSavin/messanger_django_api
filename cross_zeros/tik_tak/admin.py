from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import MyUser, Message
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.admin import UserAdmin


# Register your models here.

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    list_display = ("photo_get", "username", "email", 'is_staff', 'is_superuser',)
    # fieldsets = (
    #     (None, {'fields': ('username', 'password')}),
    #     (_('Personal info'), {'fields': ('first_name', 'last_name', 'email')}),
    #     (_('Permissions'), {
    #         'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
    #     }),
    #     (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    #     (_('Info'), {'fields': ('phone', 'city', 'photo')}),
    # )
    list_filter = ("is_staff", "is_superuser")

    def photo_get(self, obj):
        return mark_safe(f'<img src={obj.photo.url} width="20" height="25">')

    photo_get.short_description = "Фото користувача"


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ["from_user", "to_user", ]
