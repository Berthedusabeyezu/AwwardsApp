from .models import Profile, Project
from django import forms




class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ '']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 'user']
