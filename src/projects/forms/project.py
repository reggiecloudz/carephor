from django import forms

from classifications.models import Cause
from projects.models import Project

class ProjectForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    overview = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    vision = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    photo = forms.ImageField(max_length=144, required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    cause = forms.ModelChoiceField(queryset=Cause.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Project
        fields = (
            "name", 
            "overview", 
            "vision", 
            "photo",
            "cause",
        )
