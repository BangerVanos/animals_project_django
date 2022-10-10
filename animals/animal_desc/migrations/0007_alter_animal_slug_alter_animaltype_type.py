# Generated by Django 4.1.2 on 2022-10-10 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0006_alter_animalprofile_gender_alter_animaltype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='slug',
            field=models.SlugField(blank=True, default='', null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Exotic', 'Exotic'), ('None', 'None'), ('Cat', 'Cat'), ('Guinea Pig', 'Guinea Pig'), ('Fish', 'Fish'), ('Hamster', 'Hamster'), ('Dog', 'Dog'), ('Other', 'Other'), ('Parrot', 'Parrot'), ('Rabbit', 'Rabbit')], default='None', max_length=50),
        ),
    ]
