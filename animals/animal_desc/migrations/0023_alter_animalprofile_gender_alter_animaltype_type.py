# Generated by Django 4.1.2 on 2022-10-13 12:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0022_alter_animalprofile_gender_alter_animaltype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Male', 'Male'), ('Female', 'Female')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Rabbit', 'Rabbit'), ('Fish', 'Fish'), ('Hamster', 'Hamster'), ('Other', 'Other'), ('Guinea Pig', 'Guinea Pig'), ('Exotic', 'Exotic'), ('None', 'None'), ('Dog', 'Dog'), ('Parrot', 'Parrot'), ('Cat', 'Cat')], default='None', max_length=50),
        ),
    ]