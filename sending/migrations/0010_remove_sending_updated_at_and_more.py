# Generated by Django 4.2.5 on 2023-09-14 06:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0009_rename_trysending_log_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sending',
            name='updated_at',
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 14, 9, 37, 34, 896761), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(9, 37, 34, 896794), null=True, verbose_name='время рассылки'),
        ),
    ]