# Generated by Django 4.1.2 on 2022-10-16 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_userprofile_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='username',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='username',
            field=models.CharField(default=None, max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='users/avatars/'),
        ),
    ]
