from django.shortcuts import render, reverse
from django.views.generic import View, TemplateView
from django.http import HttpResponseRedirect
from . import models
from . import forms


# Create your views here.


class AnimalsView(TemplateView):
    def get(self, request, *args, **kwargs):
        animals = models.Animal.objects.filter(is_active=True)
        return render(request, "animals/animals.html", {'animals': animals})


class AnimalView(TemplateView):
    def get(self, request, *args, **kwargs):
        animal = models.Animal.objects.get(id=kwargs['anim_id'])
        animal_profile = models.AnimalProfile.objects.get(animal=animal)
        animal_photos = models.AnimalPhoto.objects.filter(animal=animal)
        return render(request, "animals/animal_desc.html",
                      {'animal': animal,
                       'animal_profile': animal_profile,
                       'animal_photos': animal_photos,
                       })


class AnimalCreateView(TemplateView):
    def get(self, request, *args, **kwargs):
        types = models.AnimalType.objects.all()
        return render(request, 'animals/animal_create.html',
                      {'animal_form': forms.AnimalCreateForm(),
                       'animal_profile_form': forms.AnimalProfileCreateForm(),
                       'animal_photos_form': forms.AnimalPhotosForm(),
                       'types': types,
                       })

    def post(self, request, *args, **kwargs):
        types = models.AnimalType.objects.all()
        photos = request.FILES.getlist('photos')
        animal_form = forms.AnimalCreateForm(request.POST, files=request.FILES)
        animal_profile_form = forms.AnimalProfileCreateForm(request.POST)
        animal_photos_form = forms.AnimalPhotosForm(request.POST, files=request.FILES)
        # check if main form is valid
        if animal_form.is_valid():
            new_animal = animal_form.save(commit=False)
            new_animal.created_by = request.user
            new_animal.type = models.AnimalType.objects.get(type=request.POST.get('type', None))
            new_animal.save()
            models.AnimalProfile.objects.create(animal=new_animal)
            # check if animal_profile form is valid
            if animal_profile_form.is_valid():
                animal_profile_form = forms.AnimalProfileCreateForm(instance=new_animal.get_profile(), data=request.POST)
                animal_profile_form.save()
                for photo in photos:
                    models.AnimalPhoto.objects.create(animal=new_animal, photo=photo)
                return HttpResponseRedirect(reverse('animals:all'))
        return render(request, 'animals/animal_create.html',
                      {'animal_form': animal_form,
                       'animal_profile_form': animal_profile_form,
                       'animal_photos_form': animal_photos_form,
                       'types': types,
                       })
