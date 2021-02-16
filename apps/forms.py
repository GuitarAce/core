from django.forms import ModelForm
from .models import ProjectTopic, Project
from django import forms

class ProjectTopicssForm(ModelForm):
    class Meta:
        model = ProjectTopic
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
