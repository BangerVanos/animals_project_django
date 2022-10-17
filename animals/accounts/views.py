from django.http import HttpResponseRedirect
from django.shortcuts import render, reverse
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from django import forms
from django.contrib import messages
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
            models.UserProfile.objects.create(user=new_user, username=f'Anonim{new_user.id}')
            if profile_form.is_valid():
                profile_form = forms.ProfileForm(instance=new_user.get_profile(), data=request.POST, files=request.FILES)
                profile_form.save(commit=False)
                if not request.POST.get('username', None):
                    try:
                        setattr(profile_form, username, f'Anonim{new_user.id}')
                    except NameError:
                        pass
                profile_form.save()
                return HttpResponseRedirect(reverse('animals:all'))
        return render(request, 'accounts/registration.html',
                      {'user_registration_form': user_registration_form,
                       'profile_form': profile_form})


# View for just looking at account info
class ProfileView(TemplateView):

    def get(self, request, *args, **kwargs):
        user_profile = request.user.get_profile()
        return render(request, 'accounts/profile.html',
                      {'profile': user_profile})


# View for changing account info
class ProfileChangeView(TemplateView):
    def get(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user)
        profile_form = forms.ProfileForm(instance=request.user.get_profile())
        return render(request, 'accounts/profile_change.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})

    def post(self, request, *args, **kwargs):
        user_form = forms.UserForm(instance=request.user, data=request.POST)
        profile_form = forms.ProfileForm(instance=request.user.get_profile(), data=request.POST,
                                         files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return HttpResponseRedirect(reverse('accounts:profile'))
        return render(request, 'accounts/profile_change.html',
                      {'user_form': user_form,
                       'profile_form': profile_form})


class LoginView(TemplateView):

    def get(self, request, *args, **kwargs):
        return render(request, 'accounts/login.html',
                      {'login_form': forms.LoginForm()})

    def post(self, request, *args, **kwargs):
        login_form = forms.LoginForm(data=request.POST)
        # raw_pass = login_form.cleaned_data.get('password')
        user = authenticate(request, username=request.POST.get('email', None), password=request.POST.get('password', None))
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('animals:all'))
        else:
            messages.error(request, 'Something went wrong!')
        return render(request, 'accounts/login.html', {'login_form': login_form})





