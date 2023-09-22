# Generated by Django 4.2.5 on 2023-09-12 09:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0004_alter_sending_start_sending_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 12, 12, 51, 26, 846860), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(12, 51, 26, 846885), null=True, verbose_name='время рассылки'),
        ),
    ]
