from django.contrib import admin # noqa
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # noqa
from django.utils.translation import gettext_lazy as _ # noqa
from . import models


# Register your models here.
class UserAdmin(BaseUserAdmin):
    """Django admin for custom user model"""
    ordering = ['name']
    list_display = ['email', 'username', 'name', 'dob', 'gender', 'country', 'state', 'city', 'pincode','date_joined']
    fieldsets = (
        (None, {'fields': ('email', 'username', 'name', 'password')}),
        (
            _('Permissions'), {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                    'is_premium_user',
                )
            }
        ),
        (
            _('Important dates'), {
                'fields': (
                    'date_joined',
                )
            }
        ),
    )
    readonly_fields = ['date_joined', 'last_login']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email',
                       'username',
                       'name',
                       'dob',
                       'gender',
                       'country',
                       'state',
                       'city',
                       'pincode',
                       'password1',
                       'password2',
                       'is_active',
                       'is_staff',
                       'is_superuser'
                       ),
        }),
    )


admin.site.register(models.UserModel, UserAdmin)
