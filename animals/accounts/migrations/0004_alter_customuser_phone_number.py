# Generated by Django 4.1.2 on 2022-10-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_is_superuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='phone_number',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
