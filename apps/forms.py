from django import forms
from .models import ClassProject

class ClassCreate(forms.ModelForm):
    class Meta:
        model = ClassProject
        fields = '__all__'