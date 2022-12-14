# Generated by Django 4.1.2 on 2022-10-10 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0013_alter_animaltype_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='animals/'),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('None', 'None'), ('Female', 'Female'), ('Male', 'Male')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Rabbit', 'Rabbit'), ('Other', 'Other'), ('Dog', 'Dog'), ('Hamster', 'Hamster'), ('Fish', 'Fish'), ('None', 'None'), ('Exotic', 'Exotic'), ('Guinea Pig', 'Guinea Pig'), ('Parrot', 'Parrot')], default='None', max_length=50),
        ),
    ]
