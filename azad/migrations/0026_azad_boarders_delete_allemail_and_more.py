# Generated by Django 4.1.4 on 2023-10-13 15:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('azad', '0025_allemail_alter_achievements_date_alter_event_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='azad_boarders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=15)),
                ('name', models.CharField(max_length=50)),
                ('emails', models.EmailField(max_length=254)),
                ('contact', models.CharField(blank=True, max_length=12)),
            ],
        ),
        migrations.DeleteModel(
            name='Allemail',
        ),
        migrations.AlterField(
            model_name='achievements',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 13, 21, 25, 15, 38986)),
        ),
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 13, 21, 25, 15, 38986)),
        ),
        migrations.AlterField(
            model_name='imagemodel',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 13, 21, 25, 15, 38986)),
        ),
        migrations.AlterField(
            model_name='notice',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 13, 21, 25, 15, 38986)),
        ),
        migrations.AlterField(
            model_name='para',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 10, 13, 21, 25, 15, 38986)),
        ),
    ]
