# Generated by Django 4.1.2 on 2022-10-17 13:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0036_alter_animalprofile_gender_alter_animaltype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('None', 'None')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Fish', 'Fish'), ('Other', 'Other'), ('Cat', 'Cat'), ('Rabbit', 'Rabbit'), ('Hamster', 'Hamster'), ('None', 'None'), ('Guinea Pig', 'Guinea Pig'), ('Parrot', 'Parrot'), ('Exotic', 'Exotic'), ('Dog', 'Dog')], default='None', max_length=50),
        ),
    ]