from django import forms
from rango.models import Rating, Movie, UserProfile
from django.contrib.auth.models import User

class MovieForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the movie name.")
    releaseDate = forms.CharField(max_length=128, help_text="Please enter the movie release date.")
    # slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Movie
        fields = ('title',)

class RatingForm(forms.ModelForm):
    rating = forms.CharField(max_length=2, help_text="Please enter your rating for the movie out of 10")
    user = forms.CharField(max_length=128, help_text="Please enter your name")

    class Meta:
        model = Rating
        exclude = ('movie',)

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')
