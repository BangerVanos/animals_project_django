from django.shortcuts import render
from django.views.generic import View, TemplateView
from . import models

# Create your views here.


class AnimalsView(TemplateView):
    def get(self, request, *args, **kwargs):
        animals = models.Animal.objects.all()
        return render(request, "animals/animals.html", {'animals': animals})

