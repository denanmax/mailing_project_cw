# Generated by Django 4.2.5 on 2023-09-20 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_email_is_confirmed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email_is_confirmed',
        ),
    ]
