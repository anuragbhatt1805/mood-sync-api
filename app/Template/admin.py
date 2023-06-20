from django.contrib import admin # noqa
from . import models

class TemplateAdmin(admin.ModelAdmin):
    """Django admin for custom user model"""
    ordering = ['name']
    search_fields = ['id', 'name', 'author']
    list_display = ['id', 'name', 'description', 'author', 'created_at', 'updated_at', 'is_active', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17']
    fieldsets = (
        (None, {'fields': (
                    'name',
                    'description',
                    'q1',
                    'q2',
                    'q3',
                    'q4',
                    'q5',
                    'q6',
                    'q7',
                    'q8',
                    'q9',
                    'q10',
                    'q11',
                    'q12',
                    'q13',
                    'q14',
                    'q15',
                    'q16',
                    'q17'
            )}),
        (
            ('Permissions'), {
                'fields': (
                    'is_active',
                )
            }
        ),
        (
            ('Important dates'), {
                'fields': (
                    'created_at',
                    'updated_at',
                )
            }
        ),
    )
    readonly_fields = ['author', 'created_at', 'updated_at']
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name',
                       'description',
                       'is_active',
                       'q1',
                       'q2',
                       'q3',
                       'q4',
                       'q5',
                       'q6',
                       'q7',
                       'q8',
                       'q9',
                       'q10',
                       'q11',
                       'q12',
                       'q13',
                       'q14',
                       'q15',
                       'q16',
                       'q17'
                       ),
        }),
    )


# Register your models here.
admin.site.register(models.Questions)
admin.site.register(models.Template, TemplateAdmin)