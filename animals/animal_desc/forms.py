from . import models
from django import forms


class AnimalCreateForm(forms.ModelForm):
    name = forms.CharField(label="Enter animal's name if there is so", widget=forms.TextInput)
    avatar = forms.ImageField(label='Upload one obligatory photo', widget=forms.FileInput)
    age = forms.IntegerField(label='Enter age(in years)', widget=forms.NumberInput)

    class Meta:
        model = models.Animal
        fields = ('name', 'avatar', 'age')


class AnimalProfileCreateForm(forms.ModelForm):
    small_desc = forms.CharField(label="Enter short description of animal", widget=forms.TextInput)
    description = forms.CharField(label="Add more information about the animal", widget=forms.Textarea)
    gender = forms.CharField(label="Enter animal's gender if you know it", widget=forms.TextInput)
    breed = forms.CharField(label="Enter breed", widget=forms.TextInput)
    where_to_get = forms.CharField(label="Enter address where animal can be grabbed", widget=forms.Textarea)

    class Meta:
        model = models.AnimalProfile
        fields = ('small_desc', 'description', 'gender', 'breed', 'where_to_get')


class AnimalPhotosForm(forms.ModelForm):
    photos = forms.ClearableFileInput(attrs={'multiple': True})

    class Meta:
        model = models.AnimalPhoto
        fields = ('photo',)

