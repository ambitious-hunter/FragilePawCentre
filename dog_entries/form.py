from django import forms
from .models import DogEntry


class DogEntryForm(forms.ModelForm):

    class Meta:
        model = DogEntry
        fields = ('title', 'image')