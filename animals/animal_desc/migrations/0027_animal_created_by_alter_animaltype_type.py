# Generated by Django 4.1.2 on 2022-10-16 15:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('animal_desc', '0026_alter_animalprofile_gender_alter_animaltype_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Guinea Pig', 'Guinea Pig'), ('Other', 'Other'), ('Rabbit', 'Rabbit'), ('Fish', 'Fish'), ('Parrot', 'Parrot'), ('Dog', 'Dog'), ('Exotic', 'Exotic'), ('None', 'None'), ('Hamster', 'Hamster'), ('Cat', 'Cat')], default='None', max_length=50),
        ),
    ]
