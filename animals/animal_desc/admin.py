from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.AnimalType)
admin.site.register(models.Animal)
admin.site.register(models.AnimalProfile)
admin.site.register(models.AnimalPhoto)
