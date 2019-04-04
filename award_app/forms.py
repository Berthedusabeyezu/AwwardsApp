from .models import Profile, Project,Votes
from django import forms




class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = [ '']

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = [ 'user','posted_on']

class VotesForm(forms.ModelForm):
    design=forms.ChoiceField(choices=((1, 1),
                                     (2, 2),
                                     (3, 3),
                                     (4, 4),
                                     (5, 5),
                                     (6, 6),
                                     (7, 7),
                                     (8, 8),
                                     (9, 9),
                                     (10, 10),))
    usability=forms.ChoiceField(choices=((1, 1),
                                     (2, 2),
                                     (3, 3),
                                     (4, 4),
                                     (5, 5),
                                     (6, 6),
                                     (7, 7),
                                     (8, 8),
                                     (9, 9),
                                     (10, 10),))
    content=forms.ChoiceField(choices=((1, 1),
                                     (2, 2),
                                     (3, 3),
                                     (4, 4),
                                     (5, 5),
                                     (6, 6),
                                     (7, 7),
                                     (8, 8),
                                     (9, 9),
                                     (10, 10),))
                                     
    class Meta:
        model = Votes
        exclude = ['user','project','posted_on']


                                