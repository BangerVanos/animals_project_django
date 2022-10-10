from django.db import models
from django.utils.text import slugify

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
    type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=50)
    avatar = models.ImageField(blank=True, null=True, upload_to=f'animals/')
    age = models.SmallIntegerField()
    slug = models.SlugField(unique=True, null=True, blank=True, default="")

    def __str__(self):
        return f"{self.name} the {self.type}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-the-{self.type}")
        super(Animal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        pass

    def get_avatar_url(self):
        if not self.avatar:
            return "front-end/static/animals/none_avatar.png/"
        else:
            return self.avatar.url


class AnimalProfile(models.Model):
    GENDERS = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')
    }
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDERS, default='None')
    breed = models.CharField(max_length=255, blank=True, null=True, default='Undefined')

    def __str__(self):
        return f"{self.animal.name}'s profile"
