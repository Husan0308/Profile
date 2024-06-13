from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import *

class UserCreationForm(forms.Form):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class PersonForm(ModelForm):
    
    class Meta:    
        model = Person 
        fields = "__all__"
    
class EducationForm(ModelForm):

    class Meta:
        model = Education 
        fields = "__all__"

class LanguageForm(ModelForm):

   
    class Meta:
        model = Language 
        fields = "__all__"

class ProfileForm(ModelForm):

    class Meta:
        model = Profile 
        fields = "__all__"

class ExperienceForm(ModelForm):

    class Meta:
        model = Experience 
        fields = "__all__"

class SkillsForm(ModelForm):

    class Meta:
        model = Skills 
        fields = "__all__"

class InterestForm(ModelForm):

    class Meta:
        model = Interest 
        fields = "__all__"
