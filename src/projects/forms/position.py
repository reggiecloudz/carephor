from django import forms

from projects.models import Position

class PositionForm(forms.ModelForm):
    title = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    people_needed = forms.IntegerField(max_value=100, min_value=1, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    requirements = forms.CharField(widget=forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}))
    
    class Meta:
        model = Position
        fields = ("title", "details", "people_needed", "requirements")
