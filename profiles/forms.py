from django.contrib.auth.models import User

from django import forms
from .models import Profile


class PostForm(forms.Form):
    text = forms.CharField()
    image = forms.FileField()

class UserUpdateForm(forms.Form):
    class Meta:
        model = User
        fields = [['username', 'last_name', 'first_name', 'email']]

class ProfileUpdateForm(forms.Form):
    
    class Meta:
        model = Profile
        fields = ['image']
