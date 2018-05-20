from django import forms
from .models import Post


class PawPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')
