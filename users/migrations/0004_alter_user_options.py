# Generated by Django 4.2.5 on 2023-09-22 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_user_email_is_confirmed'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': {('can_blocked_user', 'Can blocked user')}, 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]