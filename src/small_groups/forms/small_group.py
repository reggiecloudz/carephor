from django import forms
from classifications.models import Cause
from small_groups.models import SmallGroup

class SmallGroupForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    about = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    photo = forms.ImageField(max_length=144, required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = SmallGroup
        fields = ("name", "about", "photo",)
