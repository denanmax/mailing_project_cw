# Generated by Django 4.2.5 on 2023-09-22 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_alter_user_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': {('can_block_user', 'Can block user')}, 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]