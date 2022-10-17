# Generated by Django 4.1.2 on 2022-10-17 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0038_alter_animalprofile_gender_alter_animaltype_type'),
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
            field=models.CharField(choices=[('None', 'None'), ('Dog', 'Dog'), ('Parrot', 'Parrot'), ('Guinea Pig', 'Guinea Pig'), ('Fish', 'Fish'), ('Hamster', 'Hamster'), ('Cat', 'Cat'), ('Rabbit', 'Rabbit'), ('Other', 'Other'), ('Exotic', 'Exotic')], default='None', max_length=50),
        ),
    ]
