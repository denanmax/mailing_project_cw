# Generated by Django 4.2.5 on 2023-09-22 12:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sending', '0020_alter_sending_start_sending_date_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='log',
            options={'verbose_name': 'Журнал', 'verbose_name_plural': 'Журналы'},
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_date',
            field=models.DateField(default=datetime.datetime(2023, 9, 22, 15, 51, 33, 822329), verbose_name='Дата начала'),
        ),
        migrations.AlterField(
            model_name='sending',
            name='start_sending_time',
            field=models.TimeField(blank=True, default=datetime.time(15, 51, 33, 822360), null=True, verbose_name='время рассылки'),
        ),
    ]
