# Generated by Django 4.2.5 on 2023-09-22 11:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0018_alter_sending_start_sending_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 22, 14, 7, 17, 339878), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(14, 7, 17, 339921), null=True, verbose_name='время рассылки'),
        ),
    ]
