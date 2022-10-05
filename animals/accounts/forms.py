from django import forms
from models import CustomUser


class UserRegistrationForm(forms.ModelForm):
    username = forms.CharField(label="Enter username", widget=forms.TextInput)
    first_name = forms.CharField(label="Enter first name", widget=forms.TextInput)
    last_name = forms.CharField(label="Enter last name", widget=forms.TextInput)
    email = forms.EmailField(label="Enter your email", widget=forms.EmailInput)
    phone_number = forms.IntegerField(label="Enter your phone", widget=forms.NumberInput)
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)
    password_again = forms.CharField(label="Enter password(again)", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'password')

    def clean_password(self):
        data = self.cleaned_data
        if data['password'] != data['password_again']:
            raise forms.ValidationError("Passwords must match")
        return data['password']

    def clean_phone_number(self):
        data = self.cleaned_data
        if str(data['phone_number'])[1:2] not in ('25', '29', '33', '17') or len(str(data['phone_number'])) != 9:
            raise forms.ValidationError("Your number is not a correct Belarusian phone number")
        return data['phone_number']

