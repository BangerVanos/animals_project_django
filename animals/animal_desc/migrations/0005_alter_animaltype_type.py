# Generated by Django 4.1.2 on 2022-10-10 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0004_alter_animalprofile_gender_alter_animaltype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Hamster', 'Hamster'), ('Cat', 'Cat'), ('None', 'None'), ('Fish', 'Fish'), ('Dog', 'Dog'), ('Guinea Pig', 'Guinea Pig'), ('Exotic', 'Exotic'), ('Parrot', 'Parrot'), ('Rabbit', 'Rabbit'), ('Other', 'Other')], default='None', max_length=50),
        ),
    ]