# Generated by Django 3.2.19 on 2023-06-19 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Template', '0002_auto_20230619_0432'),
    ]

    operations = [
        migrations.AlterField(
            model_name='template',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
