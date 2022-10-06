from django.db import models

# Create your models here.


class AnimalType(models.Model):
    TYPES = {
        ('None', 'None'),
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Hamster', 'Hamster'),
        ('Guinea Pig', 'Guinea Pig'),
        ('Parrot', 'Parrot'),
        ('Rabbit', 'Rabbit'),
        ('Fish', 'Fish'),
        ('Exotic', 'Exotic'),
        ('Other', 'Other')
    }

    type = models.CharField(max_length=50, choices=TYPES, default='None')

    def __str__(self):
        return self.type


class Animal(models.Model):
    GENDERS = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')
    }
    type = models.OneToOneField(AnimalType, on_delete=models.SET_NULL)
    name = models.CharField(max_length=50)
    age = models.SmallIntegerField()
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDERS, default='None')
    breed = models.CharField(max_length=255, blank=True, null=True, default='Undefined')
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} the {self.type}"
