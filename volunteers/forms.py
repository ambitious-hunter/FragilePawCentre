from django import forms
from django.contrib.auth.forms import UserCreationForm
from volunteers.models import User
from django.core.exceptions import ValidationError


class VolunteerRegistrationForm(UserCreationForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)

    password2 = forms.CharField(label='Password Confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    # def clean_password1(self):
    #     password1 = self.cleaned_data.get('password1')
    #     password2 = self.cleaned_data.get('password2')
    #
    #     if password1 and password2 and password1 != password2:
    #         message = "Passwords do not match."
    #         raise ValidationError(message)
    #
    #     return password2
    #
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #
    #     if not email:
    #         message = "Please enter your email address"
    #         raise forms.ValidationError(message)
    #
    #     return email

    def save(self, commit=True):
        instance = super(VolunteerRegistrationForm, self).save(commit=False)

        # instance.username = instance.username

        if commit:
            instance.save()

        return instance


class VolunteerLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
