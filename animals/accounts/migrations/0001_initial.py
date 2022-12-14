# Generated by Django 4.1.2 on 2022-10-05 18:34

import accounts.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone_number', models.PositiveIntegerField(blank=True)),
                ('password', models.TextField()),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False)),
                ('join_date', models.DateTimeField(default=datetime.datetime(2022, 10, 5, 18, 34, 20, 288514, tzinfo=datetime.timezone.utc))),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', accounts.models.UserManager()),
            ],
        ),
    ]
