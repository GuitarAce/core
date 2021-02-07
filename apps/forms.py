from django.forms import ModelForm
from .models import ClassProject, Project

class ClassForm(ModelForm):
    class Meta:
        model = ClassProject
        fields = '__all__'

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'