from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AuthenticationForm(forms.Form):
    username = forms.CharField(max_length=254)
    password = forms.CharField(label=_("Password"), widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')
        if username and password:
            self.user = authenticate(username=username, password=password)
            if self.user is None:
                raise forms.ValidationError(_('User does not exist'))


class UserForm(forms.Form):
    nickname = forms.CharField(label='Nickname', max_length=100)
    age = forms.IntegerField(label='Age')

    def clean_age(self):
        age = self.cleaned_data.get('age')
        if not age % 2:
            raise ValidationError('Age should be odd')
        return age


class ApplicantForm(forms.Form):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    ENGLISH_LEVEL_CHOICES = [
        ('A1', 'A1'),
        ('A2', 'A2'),
        ('B1', 'B1'),
        ('B2', 'B2'),
        ('C1', 'C1'),
        ('C2', 'C2'),
    ]

    name = forms.CharField(label='Name', max_length=100)
    gender = forms.ChoiceField(label='Sex', choices=GENDER_CHOICES)
    age = forms.IntegerField(label='Age')
    english_level = forms.ChoiceField(label='English level', choices=ENGLISH_LEVEL_CHOICES)

    def is_valid_applicant(self):
        cleaned_data = super().clean()
        gender = cleaned_data.get('gender')
        age = cleaned_data.get('age')
        english_level = cleaned_data.get('english_level')

        if gender == 'male' and age >= 20 and english_level in ['B2', 'C1', 'C2']:
            return True
        elif gender == 'female' and age >= 22 and english_level in ['B2', 'C1', 'C2']:
            return True
        return False


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


class ChangePasswordForm(forms.Form):
    current_password = forms.CharField(widget=forms.PasswordInput, label='Current password')
    new_password1 = forms.CharField(widget=forms.PasswordInput, label='New password')
    new_password2 = forms.CharField(widget=forms.PasswordInput, label='Accept new password')

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        current_password = cleaned_data.get('current_password')
        new_password1 = cleaned_data.get('new_password1')
        new_password2 = cleaned_data.get('new_password2')

        if not self.user.check_password(current_password):
            raise forms.ValidationError('Uncorrected password.')

        if new_password1 and new_password2 and new_password1 != new_password2:
            raise forms.ValidationError('Passwords do not match.')

        return cleaned_data
