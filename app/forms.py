from .models import Genre, Track
from django import forms


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name', ]

class TrackForm(forms.ModelForm):
    class Meta:
        model = Track
        fields = ['title', 'genres','rating']