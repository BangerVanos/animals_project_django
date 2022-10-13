# Generated by Django 4.1.2 on 2022-10-13 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('animal_desc', '0019_remove_animalprofile_id_alter_animalprofile_animal_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animal',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='animal_desc.animaltype'),
        ),
        migrations.AlterField(
            model_name='animalprofile',
            name='gender',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('None', 'None'), ('Female', 'Female')], default='None', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='animaltype',
            name='type',
            field=models.CharField(choices=[('None', 'None'), ('Other', 'Other'), ('Parrot', 'Parrot'), ('Dog', 'Dog'), ('Hamster', 'Hamster'), ('Guinea Pig', 'Guinea Pig'), ('Exotic', 'Exotic'), ('Rabbit', 'Rabbit'), ('Fish', 'Fish'), ('Cat', 'Cat')], default='None', max_length=50),
        ),
    ]
