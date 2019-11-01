from .models import Profile
from django import forms
from django.forms import ModelForm
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 