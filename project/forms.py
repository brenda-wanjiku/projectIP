from django.forms import ModelForm
from .models import Profile,Project

class EditProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']


class PostProjectForm(ModelForm):
    class Meta:
        model = Project
        exclude = ['profile']