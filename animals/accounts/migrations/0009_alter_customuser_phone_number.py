# Generated by Django 4.1.2 on 2022-10-17 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_remove_customuser_username_userprofile_username_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, default=None, null=True),
        ),
    ]