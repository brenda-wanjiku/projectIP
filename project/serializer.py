from rest_framework import serializers
from .models import Project, Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'bio', 'contact', 'profile_pic')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta :
        model = Project
        fields = ('title','image', 'description','link','pubdate','profile',)