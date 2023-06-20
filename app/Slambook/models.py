from django.db import models
from django.conf import settings
from Template.models import Template

# Create your models here.

class SlambookTemplate(models.Model):
    """A slambook template class that can be used to render templates"""
    name = models.CharField(max_length=255)
    community = models.TextField(max_length=255)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    answers = models.ManyToManyField('AnswersTemplate', blank=True, null=True)
    template = models.ForeignKey(
        Template,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    objects = models.Manager()

class AnswersTemplate(models.Model):
    """A answers template class that can be used to render templates"""
    filled_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    slambook = models.ForeignKey(
        SlambookTemplate,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    a1 = models.TextField(max_length=500)
    a2 = models.TextField(max_length=500)
    a3 = models.TextField(max_length=500)
    a4 = models.TextField(max_length=500)
    a5 = models.TextField(max_length=500)
    a6 = models.TextField(max_length=500)
    a7 = models.TextField(max_length=500)
    a8 = models.TextField(max_length=500)
    a9 = models.TextField(max_length=500)
    a10 = models.TextField(max_length=500)
    a11 = models.TextField(max_length=500)
    a12 = models.TextField(max_length=500)
    a13 = models.TextField(max_length=500)
    a14 = models.TextField(max_length=500)
    a15 = models.TextField(max_length=500)
    a16 = models.TextField(max_length=500)
    a17 = models.TextField(max_length=500)
    objects = models.Manager()