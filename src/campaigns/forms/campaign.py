from django import forms
from campaigns.models import Campaign, Cause

class CampaignForm(forms.ModelForm):
    name = forms.CharField(max_length=255, min_length=3, strip=True, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    overview = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}))
    vision = forms.CharField(widget=forms.Textarea(attrs={'rows': 2, 'class': 'form-control'}))
    photo = forms.ImageField(max_length=144, required=True, widget=forms.FileInput(attrs={'class': 'form-control'}))
    financial_goal = forms.DecimalField(max_value=500000, min_value=1, max_digits=6, decimal_places=2, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    cause = forms.ModelChoiceField(queryset=Cause.objects.all(), required=True, widget=forms.Select(attrs={'class': 'form-select'}))
    
    class Meta:
        model = Campaign
        fields = (
            "name", 
            "overview", 
            "vision", 
            "photo", 
            "financial_goal",
            "cause"
        )
