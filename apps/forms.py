from django import forms
from .models import ClassPj

class ClassCreate(forms.ModelForm):
    class Meta:
        model = ClassPj
        fields = '__all__'