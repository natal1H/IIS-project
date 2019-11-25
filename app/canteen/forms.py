from django import forms
from .models import *

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class SearchForm(forms.Form):


    class Meta:
        model =Person

    pass