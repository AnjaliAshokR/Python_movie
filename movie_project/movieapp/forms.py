from django import forms
from .models import movie

class movieForm(forms.ModelForm):
    class Meta:
        model=movie
        fields=['movie_name', 'Movie_year', 'movie_desc', 'movie_img']