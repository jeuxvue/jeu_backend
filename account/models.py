from django.db import models
from django.forms import ModelForm
from django.contrib.auth.models import User
from django import forms


# # class UserRegistrationForm(forms.Form):
# class UserRegistration(models.Model):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)
#
#     # def clean_password2(self):
#     #     cd = self.clean_fields()
#     #     if cd['password'] != cd['password2']:
#     #         raise forms.ValidationError('Passwords don\'t match.')
#     #     return cd['password2']


class UserRegistrationForm(ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']
