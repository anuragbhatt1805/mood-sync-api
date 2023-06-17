from django.db import models
from django.conf import settings

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=255)
    question_type = models.CharField(max_length=50)
    objects = models.Manager()

class Template(models.Model):
    """A template class that can be used to render templates"""
    name = models.CharField(max_length=255)
    description = models.TextField(max_length=255)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=False)
    q1 = models.ForeignKey(
        Questions, related_name='question1',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q2 = models.ForeignKey(
        Questions, related_name='question2',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q3 = models.ForeignKey(
        Questions, related_name='question3',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q4 = models.ForeignKey(
        Questions, related_name='question4',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q5 = models.ForeignKey(
        Questions, related_name='question5',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q6 = models.ForeignKey(
        Questions, related_name='question6',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q7 = models.ForeignKey(
        Questions, related_name='question7',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q8 = models.ForeignKey(
        Questions, related_name='question8',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q9 = models.ForeignKey(
        Questions, related_name='question9',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    q10 = models.ForeignKey(
        Questions, related_name='question10',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    objects = models.Manager()
