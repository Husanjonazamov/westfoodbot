# Generated by Django 5.0.6 on 2024-07-04 13:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bot', '0003_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone',
        ),
    ]
