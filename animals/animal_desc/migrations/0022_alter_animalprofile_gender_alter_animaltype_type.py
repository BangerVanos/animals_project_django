# Generated by Django 4.1.2 on 2022-10-13 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0021_alter_animal_type_alter_animalprofile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Female', 'Female'), ('Male', 'Male')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('None', 'None'), ('Guinea Pig', 'Guinea Pig'), ('Parrot', 'Parrot'), ('Dog', 'Dog'), ('Fish', 'Fish'), ('Cat', 'Cat'), ('Exotic', 'Exotic'), ('Other', 'Other'), ('Hamster', 'Hamster'), ('Rabbit', 'Rabbit')], default='None', max_length=50),
        ),
    ]
