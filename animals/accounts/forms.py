from django import forms
from models import CustomUser, UserProfile
from .validators import check_photo_file_extension


class UserRegistrationForm(forms.ModelForm):
    first_name = forms.CharField(label="Enter first name", widget=forms.TextInput)
    last_name = forms.CharField(label="Enter last name", widget=forms.TextInput)
    email = forms.EmailField(label="Enter your email", widget=forms.EmailInput)
    phone_number = forms.IntegerField(label="Enter your phone", widget=forms.NumberInput)
    password = forms.CharField(label="Enter password", widget=forms.PasswordInput)
    password_again = forms.CharField(label="Enter password(again)", widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')

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


class ProfileForm(forms.ModelForm):
    username = forms.CharField(label="Enter username", widget=forms.TextInput)
    avatar = forms.ImageField(label="Upload your photo", widget=forms.ClearableFileInput,
                              validators=[check_photo_file_extension])
    biography = forms.CharField(label="Enter something about you", widget=forms.Textarea)
    date_of_birth = forms.DateField(label="Enter your date of birth", widget=forms.DateInput)

    class Meta:
        model = UserProfile
        fields = ('username', 'avatar', 'biography', 'date_of_birth')


class UserForm(forms.ModelForm):

    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'phone_number')


