from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class SearchForm(forms.Form):


    class Meta:
        model =Person

    pass


class SignUpForm(UserCreationForm):

    firstname = forms.CharField(max_length=30, required=False, help_text='First Name.')
    surname = forms.CharField(max_length=30, required=False, help_text='Surname.') 
    address = forms.CharField(max_length=30, required=False, help_text='Address.')
    email = forms.EmailField(max_length=254, help_text='Email')
    telephone = forms.CharField(max_length=30, required=False, help_text='Your phone number')

    class Meta:
        model = User
        fields = ['username', 'firstname', 'surname', 'email','address','telephone', 'password1', 'password2']