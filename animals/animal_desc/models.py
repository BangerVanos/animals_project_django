import os
from django.db import models
from django.utils.text import slugify
from datetime import datetime
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from accounts.models import CustomUser


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
    type = models.ForeignKey(AnimalType, on_delete=models.SET_NULL, null=True, default=None)
    name = models.CharField(max_length=50, blank=True, null=True)
    avatar = models.ImageField(blank=True, null=True, upload_to=f'animals/')
    age = models.SmallIntegerField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True, default="")
    create_date = models.DateField(default=timezone.now)
    created_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.name} the {self.type}"

    def save(self, *args, **kwargs):
        self.slug = slugify(f"{self.name}-the-{self.type}-{int(datetime.timestamp(datetime.now()))}")
        super(Animal, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("animals:animal_desc", kwargs={"slug": self.slug, "anim_id": self.id})

    @property
    def get_avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url
        else:
            return os.path.join(settings.STATIC_URL, 'animals/none_avatar.png/')

    def get_profile(self):
        profile = AnimalProfile.objects.get(animal=self)
        return profile


class AnimalProfile(models.Model):
    GENDERS = {
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('None', 'None')
    }
    animal = models.OneToOneField(Animal, on_delete=models.CASCADE, primary_key=True)
    small_desc = models.CharField(max_length=150, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDERS, default='None')
    breed = models.CharField(max_length=255, blank=True, null=True, default='Undefined')
    where_to_get = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.animal.slug}-{self.animal.id}'s profile"


class AnimalPhoto(models.Model):
    animal = models.ForeignKey(Animal, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=f'animals/')

    def __str__(self):
        return f"{self.animal.slug}-{self.animal.id} photo"

    @property
    def get_image_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
