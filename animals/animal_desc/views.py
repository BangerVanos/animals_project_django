from django.shortcuts import render
from django.views.generic import View, TemplateView
from . import models

# Create your views here.


class AnimalsView(TemplateView):
    def get(self, request, *args, **kwargs):
        animals = models.Animal.objects.filter(is_active=True)
        return render(request, "animals/animals.html", {'animals': animals})


class AnimalView(TemplateView):
    def get(self, request, *args, **kwargs):
        animal = models.Animal.objects.get(id=kwargs['anim_id'])
        return render(request, "animals/animal_desc.html", {'animal': animal})

