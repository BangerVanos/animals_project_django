# Generated by Django 4.1.2 on 2022-10-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='animal',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Female', 'Female'), ('Male', 'Male'), ('None', 'None')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('Exotic', 'Exotic'), ('Other', 'Other'), ('Rabbit', 'Rabbit'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Cat', 'Cat'), ('Dog', 'Dog'), ('Hamster', 'Hamster'), ('Guinea Pig', 'Guinea Pig'), ('None', 'None')], default='None', max_length=50),
        ),
    ]
