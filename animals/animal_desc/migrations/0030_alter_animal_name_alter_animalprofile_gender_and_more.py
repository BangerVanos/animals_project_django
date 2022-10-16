# Generated by Django 4.1.2 on 2022-10-16 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0029_alter_animal_created_by_alter_animalprofile_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Male', 'Male'), ('Female', 'Female')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Fish', 'Fish'), ('Other', 'Other'), ('Rabbit', 'Rabbit'), ('None', 'None'), ('Hamster', 'Hamster'), ('Dog', 'Dog'), ('Guinea Pig', 'Guinea Pig'), ('Parrot', 'Parrot'), ('Exotic', 'Exotic')], default='None', max_length=50),
        ),
    ]
