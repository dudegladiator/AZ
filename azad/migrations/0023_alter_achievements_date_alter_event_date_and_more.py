# Generated by Django 4.2.5 on 2023-10-08 11:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0022_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 8, 16, 42, 43, 222196)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 16, 42, 43, 222196)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 16, 42, 43, 222196)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 8, 16, 42, 43, 222196)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 8, 16, 42, 43, 222196)),
        ),
    ]
