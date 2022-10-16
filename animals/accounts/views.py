from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from . import forms
from . import models


class UserRegistrationView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/registration.html',
                      {'user_registration_form': forms.UserRegistrationForm(),
                       'profile_form': forms.ProfileForm()})

    def post(self, request, *args, **kwargs):
        user_registration_form = forms.UserRegistrationForm(request.POST)
        profile_form = forms.ProfileForm(request.POST, files=request.FILES)
        if user_registration_form.is_valid():
            new_user = user_registration_form.save(commit=False)
            new_user.set_password(user_registration_form.cleaned_data['password'])
            new_user.save()
            models.UserProfile.objects.create(user=new_user)
            if profile_form.is_valid():
                profile_form = forms.ProfileForm(instance=new_user.get_profile(), data=request.POST, files=request.FILES)
                profile_form.save()
                return HttpResponseRedirect(reverse('animals:all'))
        return render(request, 'accounts/registration.html',
                      {'user_registration_form': user_registration_form,
                       'profile_form': profile_form})


# View for just looking at account info
class ProfileView(TemplateView):

    def get(self, request, *args, **kwargs):
        user_profile = request.user.get_user_profile()
        return render(request, 'accounts/profile.html',
                      {'profile': user_profile})


# View for changing account info
class ProfileChangeView(TemplateView):
    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.get_user_profile())
        return render(request, 'accounts/change_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user, data=request.POST)
        profile_form = forms.ProfileForm(instance=request.user.get_user_profile(), data=request.POST,
                                         files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
        return render(request, 'accounts/change_profile.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})






