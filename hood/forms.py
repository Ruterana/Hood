from .models import Profile,Business
from django import forms
from django.forms import ModelForm
class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user'] 
class NewbusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','description'] 
