# Generated by Django 3.2.19 on 2023-06-19 08:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Template', '0003_alter_template_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='SlambookTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('community', models.TextField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('template', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='Template.template')),
            ],
        ),
        migrations.CreateModel(
            name='AnswersTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('a1', models.TextField(max_length=500)),
                ('a2', models.TextField(max_length=500)),
                ('a3', models.TextField(max_length=500)),
                ('a4', models.TextField(max_length=500)),
                ('a5', models.TextField(max_length=500)),
                ('a6', models.TextField(max_length=500)),
                ('a7', models.TextField(max_length=500)),
                ('a8', models.TextField(max_length=500)),
                ('a9', models.TextField(max_length=500)),
                ('a10', models.TextField(max_length=500)),
                ('a11', models.TextField(max_length=500)),
                ('a12', models.TextField(max_length=500)),
                ('a13', models.TextField(max_length=500)),
                ('a14', models.TextField(max_length=500)),
                ('a15', models.TextField(max_length=500)),
                ('a16', models.TextField(max_length=500)),
                ('a17', models.TextField(max_length=500)),
                ('filled_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('slambook', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Slambook.slambooktemplate')),
            ],
        ),
    ]
